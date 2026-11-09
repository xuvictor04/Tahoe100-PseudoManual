---
symbol: "DDB2"
type: "gene"
col: 5579
ensembl_id: "ENSG00000134574"
name: "damage specific DNA binding protein 2"
location: "11p11.2"
module: 62
arm: "+"
pooled_cpm: 67.94
n_lines_expressing: 48
n_dd_up: 27
n_dd_down: 34
n_dd_up_clean: 18
n_dd_down_clean: 22
in_vector_space: true
direction_upstream: 15
direction_downstream: 3
tags: ["gene", "module/062", "written"]
generated_by: "tahoemap"
---

# DDB2

*damage specific DNA binding protein 2* — 11p11.2

> [!summary] In one line
> DDB2 is the damage-recognition subunit of the UV-DDB complex and the substrate receptor of a CRL4 ubiquitin ligase, it is a direct p53 target, and it is the gene mutated in xeroderma pigmentosum group E.

## What it is

DDB2 (p48) is the small subunit of UV-DDB, the heterodimer it forms with DDB1 (p127). UV-DDB binds UV photoproducts — cyclobutane pyrimidine dimers and 6-4 photoproducts — and also abasic sites and short mismatches, with the highest affinity of any known damage sensor for the poorly helix-distorting CPD lesion. Crystallography showed how: DDB2's WD40 β-propeller holds the duplex and the damaged bases are flipped out of the helix into a hydrophobic pocket on the propeller face, which is why a lesion that barely deforms DNA can still be read. UV-DDB then hands the lesion to XPC–RAD23B to initiate global-genome nucleotide excision repair.

DDB2 has a second, inseparable job. DDB1 is the adaptor of CUL4A/CUL4B–RBX1, and DDB2 is the substrate receptor of the resulting CRL4^DDB2 ligase, which ubiquitylates XPC, core histones H2A/H3/H4 at the lesion, and DDB2 itself. The histone marks loosen nucleosomes around the damage; the autoubiquitylation drives DDB2's own proteasomal turnover and so times the handoff and terminates the response. CRL4^DDB2 activity is further gated by the COP9 signalosome after damage.

The p53 connection is at the level of expression rather than activity: DDB2 mRNA depends on basal p53 and rises further after damage in a p53-dependent way. This is the accepted explanation for a long-standing species difference — rodent cells lack appreciable UV-DDB activity and repair CPDs poorly in non-transcribed DNA, because they do not express DDB2 the way human cells do. Clinically, biallelic DDB2 loss causes xeroderma pigmentosum group E: the mildest XP complementation group, with late-onset skin cancer and without the neurological degeneration of other groups. Beyond repair, DDB2 has reported roles in oncogene-induced senescence, in CRL4-dependent transcriptional repression, and in ROS control, all on narrower evidence.

## What is uncertain

The direct-target status is secure, but what induction means functionally at 24 h is not. DDB2 protein is autoubiquitylated and short-lived at damage sites, so more mRNA does not straightforwardly mean more active UV-DDB; the limiting quantity may be CRL4 assembly or chromatin access rather than transcript abundance. The lesions DDB2 reads best are UV photoproducts, which are not what most compounds in this panel produce, so DDB2 induction here should be read as a p53 signature and not as evidence of relevant repair capacity. DDB2 also responds to inputs other than p53, and in lines with high basal replication stress its baseline may be set by those. The CRL4^DDB2-as-repressor and ROS results come from fewer systems than the repair biochemistry and should carry less weight.

## References

- Hwang et al., 1999, PNAS — showed DDB2/p48 expression depends on basal p53 and is further induced after DNA damage p53-dependently, accounting for the human/rodent difference in UV-DDB activity.
- Scrima et al., 2008, Cell — structural basis of UV DNA-damage recognition by the DDB1–DDB2 complex, with the lesion flipped into a pocket on the DDB2 β-propeller.
- Groisman et al., 2003, Cell — showed the ubiquitin ligase activity of the DDB2 and CSA complexes is differentially regulated by the COP9 signalosome in response to DNA damage.
- Sugasawa et al., 2005, Cell — UV-induced ubiquitylation of XPC mediated by the UV-DDB–ubiquitin ligase complex.
- Rapić-Otrin et al., 2003, Human Molecular Genetics — established that true xeroderma pigmentosum group E patients have a defective DDB2 component of the UV-DDB complex.

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.82× (z +14.7, q 0e+00, up in 38 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 34 drug-doses (12 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.340× (z -18.6, q 0e+00, down in 45 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FDXR]] (+0.78, fdr 7e-06), [[ANKRA2]] (+0.77, fdr 7e-06), [[POLH]] (+0.76, fdr 7e-06); moves opposite to [[CCT3]] (-0.56, fdr 1e-05), [[CCT2]] (-0.54, fdr 1e-05), [[STIP1]] (-0.54, fdr 2e-05).
> It is in [[Module 062]], a single-armed module (p53 targets up).
> Probable direction (from the cell lines, not proof of direct regulation): 15 arrows point to it, the strongest [[TP53]] → it (grade A ⚠); 3 go from it, the strongest it → [[FBXO22]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 12 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5579.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.82×** | +14.7 | 0e+00 | 38/46 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.41×** | +8.4 | 2e-14 | 28/46 (LoVo, PANC-1, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.54×** | +7.2 | 1e-10 | 28/45 (HOP62, A498, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Selinexor (drug)]] 0.05 µM |  | **1.47×** | +6.6 | 5e-09 | 30/47 (HS-578T, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.42×** | +6.1 | 1e-07 | 31/46 (SNU-1, LoVo, …) | all doses, stronger at high dose |  |
| [[Radotinib (drug)]] 5 µM |  | **1.27×** | +6.0 | 2e-07 | 28/46 (NCI-H23, LoVo, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.39×** | +5.7 | 1e-06 | 27/46 (SW48, SNU-1, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.39×** | +5.5 | 2e-06 | 25/48 (A498, SW480, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.37×** | +5.5 | 2e-06 | 26/46 (A-172, A498, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.37×** | +5.5 | 3e-06 | 27/46 (A-172, A498, …) | all doses, stronger at high dose |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.37×** | +5.4 | 3e-06 | 26/46 (C-33 A, SW480, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.30×** | +4.6 | 2e-04 | 23/46 (A549, SNU-1, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.45×** | +4.6 | 2e-04 | 22/46 (HOP62, SHP-77, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.30×** | +4.5 | 2e-04 | 25/46 (NCI-H460, SNU-1, …) | rises with dose |  |
| [[Amsacrine (drug)]] 0.5 µM |  | **1.29×** | +4.4 | 3e-04 | 22/47 (A-427, SNU-1, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.31×** | +4.3 | 5e-04 | 23/45 (NCI-H460, C32, …) | all doses, flat |  |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.28×** | +4.2 | 7e-04 | 23/46 (NCI-H460, SNU-1, …) | rises with dose |  |
| [[Amsacrine (drug)]] 5 µM |  | 1.19× | +4.2 | 8e-04 | 23/46 (A549, C32, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.17× | +3.8 | 0.003 | 17/46 (NCI-H2347, C32, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 14 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 34 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5579.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.340×** | -18.6 | 0e+00 | 45/46 (LOX-IMVI, A-427, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.479×** | -12.7 | 2e-34 | 39/46 (LOX-IMVI, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.626×** | -11.4 | 1e-27 | 30/46 (SNU-1, PANC-1, …) | rises with dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.527×** | -11.0 | 5e-26 | 38/46 (LOX-IMVI, A-172, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.524×** | -10.5 | 1e-23 | 37/46 (A-172, A549, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.559×** | -10.0 | 1e-21 | 34/46 (LOX-IMVI, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.564×** | -9.5 | 3e-19 | 39/45 (CHP-212, LoVo, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.586×** | -9.2 | 3e-18 | 32/46 (LOX-IMVI, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.591×** | -9.0 | 1e-17 | 39/46 (Panc 03.27, A549, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.603×** | -8.7 | 2e-16 | 28/47 (NCI-H23, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.422×** | -7.8 | 4e-13 | 33/42 (MIA PaCa-2, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.650×** | -7.4 | 7e-12 | 30/46 (LS 180, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.488×** | -6.5 | 5e-09 | 29/46 (HOP62, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.678×** | -6.3 | 1e-08 | 29/45 (HEC-1-A, LOX-IMVI, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.508×** | -6.1 | 4e-08 | 26/47 (Hs 766T, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.702×** | -6.1 | 5e-08 | 27/46 (SW480, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.715×** | -5.8 | 3e-07 | 26/46 (A-427, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.730×** | -5.4 | 2e-06 | 24/46 (LOX-IMVI, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.811×** | -5.1 | 1e-05 | 25/47 (A-427, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.769×** | -4.5 | 2e-04 | 25/46 (Panc 03.27, A-427, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, -0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5579. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 193 | 4 (2 ⚠) | 10 (5 ⚠) | [[Amsacrine (drug)]] 0.5 µM 2.52× (z +10.3) | [[Dinaciclib (drug)]] 5 µM 0.0465× (z -32.8) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.141× (z -21.8) |
| [[LoVo (line)]] | wt | 109 | 4 (2 ⚠) | 8 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.68× (z +11.8) | [[Auranofin (drug)]] 5 µM 0.142× (z -16.5) |
| [[NCI-H460 (line)]] | wt | 81.5 | 8 (6 ⚠) | 4 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 3.58× (z +10.7) ⚠ cell-cycle shift, explains ~23% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 0.5 µM 2.85× (z +8.8) | [[Auranofin (drug)]] 5 µM 0.226× (z -12.5) |
| [[A-172 (line)]] | wt | 171 | 2 (2 ⚠) | 9 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 2.51× (z +10.4) ⚠ cell-cycle shift, explains ~23% of this change | [[Dinaciclib (drug)]] 5 µM 0.194× (z -17.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.216× (z -17.4) |
| [[LOX-IMVI (line)]] | wt | 151 | 1 (1 ⚠) | 10 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 2.31× (z +9.1) ⚠ cell-cycle shift, explains ~23% of this change | [[Auranofin (drug)]] 5 µM 0.0843× (z -26.9) |
| [[A549 (line)]] | wt | 169 | 4 (2 ⚠) | 6 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 3.06× (z +11.1) ⚠ cell-cycle shift, explains ~23% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 2.06× (z +10.2) | [[Dinaciclib (drug)]] 5 µM 0.282× (z -12.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.325× (z -11.3) |
| [[SNU-1 (line)]] | wt | 85.5 | 8 (5 ⚠) | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 5.06× (z +11.6) ⚠ cell-cycle shift, explains ~23% of this change · without an alert: [[Amsacrine (drug)]] 0.5 µM 4.06× (z +10.0) | [[Homoharringtonine (drug)]] 5 µM 0.111× (z -22.1) ⚠ cell-cycle shift, explains ~37% of this change |
| [[SW48 (line)]] | wt | 176 | 5 (2 ⚠) | 5 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 5.58× (z +12.4) ⚠ cell-cycle shift, explains ~23% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 2.59× (z +9.7) | [[Auranofin (drug)]] 5 µM 0.165× (z -13.0) |
| [[Hs 766T (line)]] | wt | 95.8 | 0 | 8 (5 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.254× (z -10.9) |
| [[A498 (line)]] | wt | 84.5 | 4 (2 ⚠) | 3 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.01× (z +10.4) | [[Auranofin (drug)]] 5 µM 0.322× (z -11.1) |
| [[LS 180 (line)]] | wt | 139 | 3 (2 ⚠) | 4 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 3.19× (z +9.2) ⚠ cell-cycle shift, explains ~23% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 2.26× (z +9.2) | [[Panobinostat (drug)]] 5 µM 0.212× (z -12.4) |
| [[C32 (line)]] | wt | 103 | 3 (1 ⚠) | 2 | [[Amsacrine (drug)]] 5 µM 2.61× (z +10.0) | [[Auranofin (drug)]] 5 µM 0.125× (z -15.2) |
| [[MIA PaCa-2 (line)]] | alt | 43.0 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.187× (z -18.8) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.234× (z -11.5) |
| [[PANC-1 (line)]] | alt | 43.1 | 2 | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.30× (z +12.8) | [[Homoharringtonine (drug)]] 5 µM 0.288× (z -19.3) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.436× (z -9.1) |
| [[RKO (line)]] | wt | 99.9 | 4 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 0.5 µM 7.22× (z +10.8) ⚠ cell-cycle shift, explains ~70% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 3.17× (z +9.0) | [[Auranofin (drug)]] 5 µM 0.165× (z -9.8) |
| [[COLO 205 (line)]] | alt | 38.3 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.262× (z -11.8) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.226× (z -9.3) |
| [[H4 (line)]] | wt | 70.1 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.313× (z -10.7) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.194× (z -10.7) |
| [[HEC-1-A (line)]] | alt | 50.7 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.348× (z -14.1) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[TAK-901 (drug)]] 0.05 µM 0.290× (z -11.1) |
| [[hTERT-HPNE (line)]] | wt | 98.1 | 0 | 4 | — | [[Auranofin (drug)]] 5 µM 0.140× (z -12.8) |
| [[SW480 (line)]] | alt | 60.8 | 1 | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.01× (z +10.8) | [[Homoharringtonine (drug)]] 5 µM 0.438× (z -12.6) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.340× (z -11.7) |
| [[HCT15 (line)]] | alt | 42.7 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.163× (z -11.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.237× (z -9.0) |
| [[HOP62 (line)]] | alt | 32.8 | 1 | 2 (2 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.77× (z +11.2) | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -14.4) ⚠ cell-cycle shift, explains ~37% of this change |
| [[NCI-H23 (line)]] | alt | 64.3 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.117× (z -19.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.314× (z -10.5) |
| [[Panc 03.27 (line)]] | alt | 64.0 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.120× (z -17.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.296× (z -10.8) |
| [[RPMI-7951 (line)]] | alt | 39.6 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.106× (z -14.4) ⚠ cell-cycle shift, explains ~70% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.244× (z -9.0) |
| [[CFPAC-1 (line)]] | alt | 36.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.251× (z -14.7) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.308× (z -8.8) |
| [[HepG2_C3A (line)]] | wt | 51.6 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 3.85× (z +9.0) ⚠ cell-cycle shift, explains ~23% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.56× (z +8.9) | — |
| [[J82 (line)]] | alt | 60.4 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +11.6) ⚠ cell-cycle shift, explains ~37% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.297× (z -11.3) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 54.9 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.360× (z -9.3) |
| [[SW1417 (line)]] | alt | 48.0 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.33× (z +11.3) | [[Auranofin (drug)]] 5 µM 0.353× (z -9.8) |
| [[AN3 CA (line)]] | alt | 59.4 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.144× (z -9.0) |
| [[CHP-212 (line)]] | wt | 116 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0802× (z -12.0) ⚠ toxic |
| [[HT-29 (line)]] | alt | 28.7 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.275× (z -8.8) |
| [[KATO III (line)]] | alt | 43.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.245× (z -11.4) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 22.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.79× (z +9.4) | — |
| [[SHP-77 (line)]] | alt | 36.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.06× (z +10.1) | — |
| [[SK-MEL-2 (line)]] | alt | 38.8 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.239× (z -10.1) |
| [[SNU-423 (line)]] | alt | 44.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -14.2) ⚠ cell-cycle shift, explains ~37% of this change |
| [[AsPC-1 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 15.6 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 55.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 58.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 65.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 37.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 53.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 16.2 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5579), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FDXR]] | +0.78 | +0.74 / +0.82 | both halves | 7e-06 | pathway: HALLMARK_P53_PATHWAY; STRING 730 |
| [[ANKRA2]] | +0.77 | +0.74 / +0.73 | both halves | 7e-06 | pathway: HALLMARK_P53_PATHWAY |
| [[POLH]] | +0.76 | +0.76 / +0.78 | both halves | 7e-06 | same gene group; pathway: HALLMARK_DNA_REPAIR |
| [[PPM1D]] | +0.74 | +0.73 / +0.69 | both halves | 7e-06 | pathway: HALLMARK_P53_PATHWAY; STRING 456 |
| [[ACTA2]] | +0.71 | +0.67 / +0.70 | both halves | 7e-06 |  |
| [[MDM2]] | +0.68 | +0.55 / +0.71 | both halves | 1e-05 | pathway: HALLMARK_P53_PATHWAY; STRING 550 |
| [[RPS27L]] | +0.68 | +0.63 / +0.68 | both halves | 7e-06 | pathway: HALLMARK_P53_PATHWAY; STRING 471 |
| [[FAS]] | +0.68 | +0.54 / +0.68 | both halves | 1e-05 | pathway: HALLMARK_P53_PATHWAY |
| [[GRIN2C]] | +0.67 | +0.56 / +0.66 | both halves | 1e-05 |  |
| [[TYMSOS]] | +0.67 | +0.53 / +0.65 | both halves | 1e-05 |  |
| [[DCP1B]] | +0.65 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[PHPT1]] | +0.64 | +0.59 / +0.70 | both halves | 7e-06 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCT3]] | -0.56 | -0.53 / -0.55 | both halves | 1e-05 |  |
| [[CCT2]] | -0.54 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[STIP1]] | -0.54 | -0.47 / -0.56 | both halves | 2e-05 |  |
| [[TALDO1]] | -0.53 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[HERC2]] | -0.52 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[RABGAP1L]] | -0.52 | -0.50 / -0.42 | both halves | 4e-05 |  |
| [[RSU1]] | -0.51 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[CCT5]] | -0.51 | -0.49 / -0.57 | both halves | 1e-05 |  |
| [[NUDC]] | -0.50 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[ST6GALNAC4]] | -0.50 | -0.43 / -0.39 | both halves | 6e-05 |  |
| [[TCP1]] | -0.50 | -0.46 / -0.49 | both halves | 2e-05 |  |
| [[PRELID3B]] | -0.50 | -0.50 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 2, B 10, C 3. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TP53]] | A | TP53 activity raises DDB2's level | recorded loss-of-function mutation of TP53 in 33 lines vs 17 not recorded | 2.72× lower at baseline in the TP53-altered lines | 4e-04 | ⚠ within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines |
| [[TP53]] | A | TP53 activity strengthens DDB2's drug response | recorded loss-of-function mutation of TP53 in 29 lines vs 17 not recorded | the TP53-altered lines respond 0.68× as strongly (z diff +1.89); strongest at Belinostat 5 µM: 0.70x vs 0.38x (z diff +4.8) | 0.014 | ⚠ within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines; target measured in part of the lines; lower baseline (lost expression?); artifact flags |
| [[PINCR]] | B | PINCR activity raises DDB2's level | lines that do not express PINCR (29) vs lines expressing it (21) | 2.15× lower at baseline in the lines without PINCR | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PTCHD4, ENSG00000269729, PCK1 |
| [[TOP2A]] | B | TOP2A activity lowers DDB2's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 4.5% of all compounds | 0.005 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[ACTA2]] | B | ACTA2 activity raises DDB2's level | lines that do not express ACTA2 (11) vs lines expressing it (39) | 2.12× lower at baseline in the lines without ACTA2 | 0.012 | ⚠ within organs, on part of the lines; also absent: FAS; maybe low, not absent |
| [[GRIN2C]] | B | GRIN2C activity raises DDB2's level | lines that do not express GRIN2C (14) vs lines expressing it (36) | 1.87× lower at baseline in the lines without GRIN2C | 0.034 | ⚠ within organs, on part of the lines; also absent: FDXR, CYFIP2, GDF15; maybe low, not absent |
| [[EDA2R]] | B | EDA2R activity raises DDB2's level | lines that do not express EDA2R (28) vs lines expressing it (22) | 1.46× lower at baseline in the lines without EDA2R | 0.043 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000253503, SLC6A15, WNK3 |
| [[FDXR]] | B | FDXR activity raises DDB2's level | lines that do not express FDXR (8) vs lines expressing it (42) | 2.09× lower at baseline in the lines without FDXR | 0.049 | ⚠ within organs, on part of the lines; also absent: GRIN2C, MCM10; maybe low, not absent |
| [[TP53INP1]] | B | TP53INP1 activity raises DDB2's level | lines that do not express TP53INP1 (7) vs lines expressing it (43) | 1.82× lower at baseline in the lines without TP53INP1 | 0.054 | ⚠ within organs, on part of the lines; also absent: ENSG00000251379; maybe low, not absent |
| [[PINCR]] | B | PINCR activity strengthens DDB2's drug response | lines that do not express PINCR (27) vs lines expressing it (19) | the lines without PINCR respond 0.70× as strongly (z diff +1.57); strongest at Panobinostat 5 µM: 0.66x vs 0.39x (z diff +3.7) | 0.069 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PTCHD4, ENSG00000269729, PCK1; target measured in part of the lines; artifact flags |
| [[PTCHD4]] | B | PTCHD4 activity raises DDB2's level | lines that do not express PTCHD4 (33) vs lines expressing it (17) | 1.76× lower at baseline in the lines without PTCHD4 | 0.079 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PINCR, MIR99AHG, NETO1 |
| [[PURPL]] | B | PURPL activity raises DDB2's level | lines that do not express PURPL (25) vs lines expressing it (25) | 1.60× lower at baseline in the lines without PURPL | 0.090 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MIR99AHG, ENSG00000286385, RPS4Y1 |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FBXO22]] | C | DDB2's natural level strengthens FBXO22's drug response | DDB2's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.65, reverse +0.51; direction not clear | 0.043 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[GPX1]] | C | DDB2's natural level strengthens GPX1's drug response | DDB2's natural level across 43 lines (lineage-adjusted; a glimpse) | r +0.67, reverse +0.08; direction not clear | 0.073 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[TMEM68]] | C | DDB2's natural level strengthens TMEM68's drug response | DDB2's natural level across 46 lines (lineage-adjusted; a glimpse) | r +0.63, reverse +0.07; direction not clear | 0.089 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

## Where it sits

- **Module**: [[Module 062]] — p53 targets up; 78 genes; every member is in the + arm (projection on the module's main direction 0.779). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-15.9, 36.0); signed map (41.4, -24.7). **Vector** length 142, 47.4% of its response variance represented; |z| ≥ 3 in 1,724 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *TP53 Regulates Transcription of Cell Death Genes* (reactome, mean cos +0.57 to 6); *apoptosis* (hallmark, mean cos +0.56 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +10.3 | +7.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.7 | +14.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | +9.6 | +5.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +9.1 | +5.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~41% of this change | +8.4 | +3.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.7 | +1.4 |
|  | [[Amsacrine (drug)]] 5 µM |  | +5.4 | +4.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +5.3 | +4.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | +4.7 | +4.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.4 | +2.3 |
| fall | [[Auranofin (drug)]] 5 µM |  | -10.2 | -18.6 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -6.3 | -10.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -5.3 | -12.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.2 | -11.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.8 | -9.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.6 | -6.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.5 | -3.9 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -3.2 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | damage specific DNA binding protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p11.2 — chr11:47,214,465-47,239,217 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DDBB, UV-DDB2, FLJ34321, XPE |
| Gene groups (HGNC) | WD repeat domain containing; Xeroderma pigmentosum complementation groups; Nucleotide excision repair |
| Hallmark sets | DNA_REPAIR, P53_PATHWAY |
| Reactome | 11 pathways, smallest: DNA Damage Recognition in GG-NER; Dual Incision in GG-NER; Formation of Incision Complex in GG-NER |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92466](https://www.uniprot.org/uniprotkb/Q92466) (DNA damage-binding protein 2):

> Protein, which is both involved in DNA repair and protein ubiquitination, as part of the UV-DDB complex and DCX (DDB1-CUL4-X-box) complexes, respectively. Core component of the UV-DDB complex (UV-damaged DNA-binding protein complex), a complex that recognizes UV-induced DNA damage and recruit proteins of the nucleotide excision repair pathway (the NER pathway) to initiate DNA repair. The UV-DDB complex preferentially binds to cyclobutane pyrimidine dimers (CPD), 6-4 photoproducts (6-4 PP), …

**Summary**, from NCBI Gene [1643](https://www.ncbi.nlm.nih.gov/gene/1643):

> This gene encodes a protein that is necessary for the repair of ultraviolet light-damaged DNA. This protein is the smaller subunit of a heterodimeric protein complex that participates in nucleotide excision repair, and this complex mediates the ubiquitylation of histones H3 and H4, which facilitates the cellular response to DNA damage. This subunit appears to be required for DNA binding. Mutations in this gene cause xeroderma pigmentosum complementation group E, a recessive disease that is …

**Accessions** — [HGNC:2718](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2718) · Entrez [1643](https://www.ncbi.nlm.nih.gov/gene/1643) · UniProt [Q92466](https://www.uniprot.org/uniprotkb/Q92466) · Ensembl [ENSG00000134574](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134574)

## Data

Gene col 5579: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5579); `tables/drug_effects.parquet` (76 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5579, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5579]; `tensor/DDL_lfc|DDL_z.npy` [5579]; `embed/gene_vectors.npy` [5579]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5579 or target_col == 5579). Every well: [[DDB2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. The written part above is `tahoemap/vault_seed/genes/DDB2.md`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
