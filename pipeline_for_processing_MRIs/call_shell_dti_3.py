patients = ["135_S_4309", "135_S_4281", "131_S_0123", "129_S_4422", "129_S_4396", "129_S_4371", "129_S_4369", "129_S_4287", "129_S_2347", "129_S_2332", "129_S_0778", "127_S_5266", "127_S_5228", "127_S_5185", "127_S_5132", "127_S_5095", "127_S_5067", "127_S_5058", "127_S_5056", "127_S_5028", "127_S_4992", "127_S_4940", "127_S_4928", "127_S_4844", "127_S_4843", "127_S_4765", "127_S_4645", "127_S_4624", "127_S_4604", "127_S_4500", "127_S_4301", "127_S_4240", "127_S_4210", "127_S_4198", "127_S_4197", "127_S_4148", "127_S_2234", "127_S_2213", "126_S_5243", "126_S_5214", "126_S_4896", "126_S_4891", "126_S_4712", "126_S_4686", "126_S_4675", "126_S_4514", "126_S_4507", "126_S_4494", "126_S_4458", "126_S_2407", "126_S_2405", "126_S_2360", "109_S_4594", "109_S_4531", "109_S_4499", "109_S_4455", "109_S_4380", "109_S_2200", "099_S_4565", "099_S_4498", "099_S_4480", "099_S_4463", "099_S_4205", "099_S_4157", "099_S_4104", "099_S_4086", "099_S_4076", "099_S_2146", "099_S_2063", "098_S_4506", "098_S_4275", "098_S_4215", "098_S_4201", "098_S_4018", "098_S_4003", "098_S_2079", "098_S_2052", "098_S_2047", "094_S_4858", "094_S_4649", "094_S_4630", "094_S_4560", "094_S_4503", "094_S_4282", "094_S_4234", "094_S_4162", "094_S_4089", "094_S_2367", "094_S_2238", "094_S_2216", "094_S_2201", "057_S_5292", "057_S_4909", "057_S_4897", "057_S_4888", "057_S_2398", "057_S_0934", "052_S_5062", "052_S_4959", "052_S_4945", "052_S_4944", "052_S_4885", "052_S_4807", "052_S_4626", "052_S_2249", "052_S_1352", "052_S_1346", "052_S_0671", "029_S_5219", "029_S_5166", "029_S_5158", "029_S_4652", "029_S_4585", "029_S_4385", "029_S_4384", "029_S_4307", "029_S_4290", "029_S_4279", "027_S_5277", "027_S_5197", "027_S_5169", "027_S_5127", "027_S_5118", "027_S_5110", "027_S_5109", "027_S_5093", "027_S_5083", "027_S_5079", "027_S_4964", "027_S_4962", "027_S_4955", "027_S_4938", "027_S_4936", "027_S_4926", "027_S_4919", "027_S_4873", "027_S_4869", "027_S_4802", "027_S_4801", "027_S_4757", "027_S_4729", "027_S_2336", "027_S_2245", "027_S_2219", "027_S_2183", "021_S_5237", "021_S_5236", "021_S_5194", "021_S_5177", "021_S_5129", "021_S_5099", "021_S_4924", "021_S_4857", "021_S_4744", "021_S_4718", "021_S_4659", "021_S_4558", "021_S_4421", "021_S_4419", "021_S_4402", "021_S_4335", "021_S_4276", "021_S_4254", "021_S_4245", "021_S_2125", "021_S_2124", "021_S_2100", "021_S_2077", "016_S_5251", "016_S_5057", "016_S_5032", "016_S_5031", "016_S_5007", "016_S_4952", "016_S_4951", "016_S_4902", "016_S_4887", "016_S_4688", "016_S_4646", "016_S_4638", "016_S_4591", "016_S_4584", "016_S_4583", "016_S_4353", "016_S_4121", "016_S_4097", "016_S_4009", "016_S_2031", "007_S_5265", "007_S_5196", "007_S_4911", "007_S_4637", "007_S_4620", "007_S_4568", "007_S_4516", "007_S_4488", "007_S_4467", "007_S_4387", "007_S_4272", "007_S_2394", "007_S_2106", "005_S_5119", "005_S_5038", "005_S_4910", "005_S_4707", "005_S_4185", "005_S_4168", "005_S_2390", "005_S_0610", "003_S_5187", "003_S_5165", "003_S_5130", "003_S_4900", "003_S_4892", "003_S_4872", "003_S_4644", "003_S_4555", "003_S_4441", "003_S_4373", "003_S_4350", "003_S_4288", "003_S_4136", "003_S_4119", "003_S_4081", "003_S_2374", "003_S_1074", "003_S_0908"]

import subprocess

for i in patients:
	# Structural MRI segmentation
	arguments = [i, "~/ALEX/IMAGES/MRI/" + i + "/ADNI_" + i + ".nii", "~/ALEX/IMAGES/MRI/" + i + "/MRI_CORRECTED"]
	cmd = subprocess.Popen("~/ALEX/CODE/FastSurfer.sh %s %s %s" % (str(arguments[0]),str(arguments[1]), str(arguments[2]),), shell=True)
	cmd.wait()
	
	# Extract b-vals and b-vecs
	arg = "~/ALEX/IMAGES/DTI/" + i + "/a"
	cmd = subprocess.Popen("~/ALEX/CODE/call_dcm2nii.sh %s" % (str(arg),), shell=True)
	cmd.wait()
	
	# DTI pre-processing
	arguments = ["a", "~/ALEX/IMAGES/MRI/" + i + "/MRI_CORRECTED", "~/ALEX/IMAGES/MRI/" + i + "/MRI_CORRECTED/a.nii.gz", "~/ALEX/IMAGES/MRI/" + i + "/MRI_CORRECTED/a.bval", "~/ALEX/IMAGES/MRI/" + i + "/MRI_CORRECTED/a.bvec"]
	cmd = subprocess.Popen("~/ALEX/CODE/DT_recon_2.sh %s %s %s %s %s" % (str(arguments[0]),str(arguments[1]), str(arguments[2]),str(arguments[3]),str(arguments[4]),), shell=True)
	cmd.wait()
	
	# New Segmentation of the file aparc.DKTatlas+aseg.nii.gz
	arg = "~/ALEX/IMAGES/MRI/" + i + "/MRI_CORRECTED/recon_all/mri/aparc.DKTatlas+aseg.nii.gz"
	cmd = subprocess.Popen("~/ALEX/CODE/call_change_segmentation.sh %s" % (str(arg),), shell=True)
	cmd.wait()
	
	# Fibre Tracking
	arguments = [i, "~/ALEX/IMAGES/MRI/" + i + "/MRI_CORRECTED"]
	cmd = subprocess.Popen("~/ALEX/CODE/Tracking.sh %s %s" % (str(arguments[0]),str(arguments[1]),), shell=True)
	cmd.wait()

	# Quality Control
	arg = ["~/ALEX/IMAGES/MRI/" + i + "/MRI_CORRECTED", "~/ALEX/CODE/qc/qc" + i]
	cmd = subprocess.Popen("~/ALEX/CODE/call_qc_alex.sh %s %s" % (str(arg[0]), str(arg[1])), shell=True)
	cmd.wait()

	# Feature Extraction
	arg = ["~/ALEX/IMAGES/MRI/" + i + "/MRI_CORRECTED", "/media/extop/B71E-9FCD/matrices/matrix" + i + ".csv"]
	cmd = subprocess.Popen("~/ALEX/CODE/call_extract_intrainter.sh %s %s" % (str(arg[0]), str(arg[1])), shell=True)
	cmd.wait()
                

