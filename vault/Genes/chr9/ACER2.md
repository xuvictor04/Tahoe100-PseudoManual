---
symbol: "ACER2"
type: "gene"
col: 10787
ensembl_id: "ENSG00000177076"
name: "alkaline ceramidase 2"
location: "9p22.1"
module: 62
arm: "+"
pooled_cpm: 16.02
n_lines_expressing: 49
n_dd_up: 31
n_dd_down: 19
n_dd_up_clean: 19
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 8
direction_downstream: 0
tags: ["gene", "module/062", "written"]
generated_by: "tahoemap"
---

# ACER2

*alkaline ceramidase 2* — 9p22.1

> [!summary] In one line
> ACER2 is a Golgi alkaline ceramidase that hydrolyses ceramide to sphingosine, and it is one of the most cleanly p53-inducible genes in sphingolipid metabolism.

## What it is

ACER2 (alkaline ceramidase 2) is one of three human alkaline ceramidases. It is a multi-pass membrane enzyme of the Golgi that hydrolyses unsaturated long-chain ceramides and dihydroceramides into a free fatty acid plus sphingosine or dihydrosphingosine; its activity is reported to depend on calcium and to have an alkaline pH optimum. Sphingosine released this way is the substrate for the sphingosine kinases, so ACER2 sits at a control point in the sphingolipid rheostat: it drains the ceramide pool, which signals toward arrest and death, and feeds the sphingosine and sphingosine-1-phosphate pools, which signal toward survival and migration. Which of those two consequences dominates depends on how much flux passes through the step.

Its regulation is what makes it interesting here. ACER2 mRNA rises sharply after DNA damage, and the induction appears to be a direct p53 effect: the dominant promoter lies inside the first intron and carries p53 consensus sites, and mutating the first conserved site abolishes p53-driven reporter activity. Downstream, doxorubicin raises ACER2 and cellular sphingosine together in a dose-dependent way, knockdown blunts both the sphingosine rise and the death response, and forced ACER2 expression drives autophagy and apoptosis in a manner blocked by antioxidants. Clinically, nothing is established: ACER2 is not a drug target and has no accepted diagnostic role.

## What is uncertain

The direct-target claim rests on reporter and ChIP work in a small number of lines, and the intronic-promoter architecture has not been widely replicated; the question of whether some of the induction is indirect remains open. More importantly for reading this vault, a transcript increase is a weak proxy for ceramidase flux, which also depends on substrate supply, kinase levels and Golgi context. The cell-fate consequence is dose-dependent in the reported work — strong induction linked to death, modest induction linked to blunted arrest through S1P — and nothing in a 24 h mRNA measurement says which regime a given exposure occupied. Whether ACER2 is an effector of p53-driven death or only a bystander readout of it has been tested by knockdown in very few systems.

## References

- Wang et al., 2017, Scientific Reports — identified ACER2 as a direct p53 target with its major promoter and p53 sites in the first intron, and showed ROS-dependent autophagy and apoptosis on overexpression.
- Xu et al., 2016, Oncotarget — showed doxorubicin raises ACER2 and sphingosine dose-dependently in HCT116, and that ACER2 knockdown blunts both the sphingosine rise and the death response.

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (12 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.36× (z +12.0, q 3e-30, up in 37 of 46 measured lines) ⚠ cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.75× (z +11.0, q 1e-25, up in 25 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (8 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 0.488× (z -9.6, q 3e-19, down in 29 of 40 measured lines) ⚠ toxic. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.647× (z -6.1, q 1e-07, down in 25 of 46 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GDF15]] (+0.70, fdr 1e-05), [[PINCR]] (+0.65, fdr 1e-05), [[GRIN2C]] (+0.65, fdr 1e-05); moves opposite to [[PTCD2]] (-0.46, fdr 2e-04), [[CS]] (-0.44, fdr 6e-05), [[USP24]] (-0.44, fdr 3e-05).
> It is in [[Module 062]], a single-armed module (p53 targets up).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[TP53]] → it (grade A ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 12 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10787.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **2.36×** | +12.0 | 3e-30 | 37/46 (SW1417, J82, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.75×** | +11.0 | 1e-25 | 25/44 (A498, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.17×** | +10.8 | 7e-25 | 38/46 (J82, SW480, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.63×** | +9.7 | 4e-20 | 36/46 (SW480, J82, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **2.00×** | +9.7 | 4e-20 | 32/46 (SW1417, HOP62, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.57×** | +8.9 | 8e-17 | 30/47 (A498, A549, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.81×** | +8.3 | 9e-15 | 30/46 (A498, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.73×** | +7.6 | 1e-12 | 32/46 (HOP62, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.72×** | +7.3 | 2e-11 | 26/45 (A498, A549, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.68×** | +7.2 | 3e-11 | 26/46 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~45% of this change | **1.63×** | +6.6 | 2e-09 | 21/40 (A498, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.61×** | +6.4 | 8e-09 | 24/43 (A498, NCI-H460, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.36×** | +6.1 | 6e-08 | 23/46 (A498, J82, …) | top dose only | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.51×** | +5.7 | 5e-07 | 21/45 (A498, RKO, …) | all doses, stronger at high dose |  |
| [[Amsacrine (drug)]] 5 µM |  | **1.29×** | +5.0 | 2e-05 | 21/46 (RKO, A498, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.39×** | +4.6 | 1e-04 | 17/44 (SW1417, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.37×** | +4.4 | 3e-04 | 20/46 (NCI-H460, RKO, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.34×** | +4.1 | 0.002 | 18/46 (NCI-H460, RKO, …) | rises with dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.71×** | +3.9 | 0.003 | 7/43 (SW480, HOP62, …) | rises with dose | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.69×** | +3.8 | 0.003 | 9/47 (SW480, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.05 µM |  | **1.31×** | +3.7 | 0.005 | 10/46 (A549, A498, …) | all doses, stronger at high dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.61×** | +3.5 | 0.012 | 7/44 (SW480, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Amsacrine (drug)]] 0.5 µM |  | **1.26×** | +3.3 | 0.024 | 14/47 (NCI-H460, A549, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10787.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.488×** | -9.6 | 3e-19 | 29/40 (LoVo, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.524×** | -8.7 | 1e-15 | 29/45 (SK-MEL-2, HEC-1-A, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.571×** | -7.8 | 9e-13 | 24/36 (LS 180, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.589×** | -7.4 | 2e-11 | 26/46 (LoVo, SK-MEL-2, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.647×** | -6.1 | 1e-07 | 25/46 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.672×** | -5.5 | 3e-06 | 20/45 (SW 900, KATO III, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.683×** | -5.1 | 2e-05 | 16/29 (LOX-IMVI, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.718×** | -4.6 | 3e-04 | 20/46 (NCI-H460, A549, …) | two highest doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.821×** | -3.9 | 0.006 | 15/46 (AN3 CA, NCI-H1792, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.759×** | -3.8 | 0.007 | 18/46 (NCI-H460, C32, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.591×** | -3.8 | 0.007 | 8/44 (NCI-H460, J82, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.593×** | -3.8 | 0.007 | 18/43 (Hs 766T, SK-MEL-2, …) | rises with dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **0.769×** | -3.7 | 0.011 | 18/42 (SK-MEL-2, HEC-1-A, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.617×** | -3.5 | 0.017 | 16/46 (KATO III, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 0.842× | -3.4 | 0.027 | 12/46 (HCT15, RKO, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.647×** | -3.2 | 0.047 | 13/44 (SK-MEL-2, J82, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.652×** | -3.1 | 0.053 | 10/44 (Panc 03.27, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.05 µM |  | **0.808×** | -3.0 | 0.082 | 12/46 (SW 1271, NCI-H661, …) | inconsistent across doses |  |
| [[venetoclax (drug)]] 5 µM |  | **0.671×** | -2.9 | 0.097 | 10/40 (HOP62, J82, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.49 per unit of S-phase module lfc, -0.51 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10787. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 15.9 | 9 (7 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 15.4× (z +15.7) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.29× (z +14.0) | — |
| [[LS 180 (line)]] | wt | 29.3 | 4 (3 ⚠) | 5 (5 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.82× (z +12.6) | [[Dinaciclib (drug)]] 0.5 µM 0.0415× (z -21.1) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 31.0 | 3 (1 ⚠) | 4 (4 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 5.59× (z +11.2) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 2.78× (z +9.7) | [[Dinaciclib (drug)]] 5 µM 0.144× (z -12.7) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 23.9 | 4 (3 ⚠) | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.21× (z +13.4) | [[Niclosamide (olamine) (drug)]] 5 µM 0.0978× (z -14.7) ⚠ toxic |
| [[NCI-H460 (line)]] | wt | 15.3 | 5 (4 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.72× (z +11.7) | [[Dinaciclib (drug)]] 5 µM 0.182× (z -10.4) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 10.9 | 1 | 3 (3 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.63× (z +9.2) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.221× (z -10.3) ⚠ cell-cycle shift, explains ~24% of this change |
| [[HEC-1-A (line)]] | alt | 13.5 | 0 | 3 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.148× (z -11.3) ⚠ cell-cycle shift, explains ~31% of this change |
| [[KATO III (line)]] | alt | 59.5 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.241× (z -12.2) ⚠ cell-cycle shift, would explain all of this change |
| [[RKO (line)]] | wt | 24.9 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 9.87× (z +11.2) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 3.44× (z +8.6) | — |
| [[SW 900 (line)]] | alt | 23.0 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.157× (z -10.6) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 24.0 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0856× (z -11.5) ⚠ toxic; transcription drop · without an alert: [[Roxadustat (drug)]] 0.05 µM 0.100× (z -10.0) |
| [[HT-29 (line)]] | alt | 33.5 | 0 | 2 (2 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.120× (z -12.1) ⚠ transcription drop; cell-cycle shift, explains ~87% of this change |
| [[hTERT-HPNE (line)]] | wt | 21.1 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.42× (z +9.7) | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.0675× (z -11.6) |
| [[LOX-IMVI (line)]] | wt | 24.2 | 1 (1 ⚠) | 1 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 4.33× (z +9.2) ⚠ cell-cycle shift, explains ~34% of this change | [[Dinaciclib (drug)]] 5 µM 0.0961× (z -14.7) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 23.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.186× (z -8.5) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 14.6 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0937× (z -12.5) ⚠ toxic |
| [[BT-474 (line)]] | alt | 11.0 | 0 | 1 | — | [[Hydroxyurea (drug)]] 0.05 µM 0.0763× (z -9.6) |
| [[HCT15 (line)]] | alt | 13.9 | 0 | 1 | — | [[Belumosudil (drug)]] 5 µM 0.0613× (z -10.2) |
| [[Hs 766T (line)]] | wt | 13.5 | 0 | 1 (1 ⚠) | — | [[Allantoin (drug)]] 0.05 µM 0.0693× (z -12.8) ⚠ transcription drop |
| [[J82 (line)]] | alt | 15.7 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.24× (z +8.6) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 8.64 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0643× (z -11.4) ⚠ toxic |
| [[NCI-H1792 (line)]] | alt | 10.7 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0719× (z -13.0) ⚠ transcription drop; cell-cycle shift, explains ~87% of this change |
| [[NCI-H23 (line)]] | alt | 13.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -10.3) ⚠ cell-cycle shift, would explain all of this change |
| [[Panc 03.27 (line)]] | alt | 20.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.124× (z -11.3) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 7.70 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.196× (z -10.4) ⚠ cell-cycle shift, explains ~31% of this change |
| [[SK-MEL-2 (line)]] | alt | 20.3 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.124× (z -11.3) ⚠ cell-cycle shift, explains ~31% of this change |
| [[SW1417 (line)]] | alt | 16.0 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.78× (z +8.8) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[AN3 CA (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.43 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.40 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.87 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.22 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.65 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.33 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.46 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.21 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.80 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.39 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.26 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 15.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10787), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 5 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GDF15]] | +0.70 | +0.55 / +0.71 | both halves | 1e-05 | **novel candidate** |
| [[PINCR]] | +0.65 | +0.57 / +0.69 | both halves | 1e-05 |  |
| [[GRIN2C]] | +0.65 | +0.50 / +0.68 | both halves | 1e-05 |  |
| [[CDKN1A]] | +0.64 | +0.52 / +0.65 | both halves | 1e-05 |  |
| [[POLH]] | +0.61 | +0.57 / +0.63 | both halves | 1e-05 |  |
| [[TIGAR]] | +0.59 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[FDXR]] | +0.59 | +0.45 / +0.62 | both halves | 3e-05 |  |
| [[INSYN2A]] | +0.58 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[ADAMTS7]] | +0.56 | +0.38 / +0.61 | both halves | 6e-05 |  |
| [[DNAI3]] | +0.55 | +0.34 / +0.63 | both halves | 1e-04 |  |
| [[RPS27L]] | +0.55 | +0.44 / +0.61 | both halves | 3e-05 |  |
| [[TNFRSF10A]] | +0.55 | +0.46 / +0.56 | both halves | 3e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTCD2]] | -0.46 | -0.32 / -0.43 | both halves | 2e-04 |  |
| [[CS]] | -0.44 | -0.39 / -0.49 | both halves | 6e-05 |  |
| [[USP24]] | -0.44 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[PUS7L]] | -0.43 | -0.34 / -0.48 | both halves | 1e-04 |  |
| [[AIFM1]] | -0.42 | -0.32 / -0.40 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 1, B 6, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TP53]] | A | TP53 activity strengthens ACER2's drug response | recorded loss-of-function mutation of TP53 in 30 lines vs 17 not recorded | the TP53-altered lines respond 0.81× as strongly (z diff +0.74); strongest at Idarubicin (hydrochloride) 5 µM: 1.25x vs 2.80x (z diff +6.0) | 9e-04 | ⚠ within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines; target measured in part of the lines; artifact flags |
| [[TOP2A]] | B | TOP2A activity lowers ACER2's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 5.0% of all compounds | 0.005 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[PINCR]] | B | PINCR activity strengthens ACER2's drug response | lines that do not express PINCR (28) vs lines expressing it (19) | the lines without PINCR respond 0.79× as strongly (z diff +0.75); strongest at Idarubicin (hydrochloride) 5 µM: 1.30x vs 2.41x (z diff +4.8) | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PTCHD4, ENSG00000269729, PCK1; target measured in part of the lines; artifact flags |
| [[PTCHD4]] | B | PTCHD4 activity strengthens ACER2's drug response | lines that do not express PTCHD4 (32) vs lines expressing it (15) | the lines without PTCHD4 respond 1.04× as strongly (z diff +0.10); strongest at Idarubicin (hydrochloride) 5 µM: 1.40x vs 2.54x (z diff +4.2) | 0.041 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PINCR, MIR99AHG, NETO1; target measured in part of the lines; both ways; artifact flags |
| [[GRIN2C]] | B | GRIN2C activity raises ACER2's level | lines that do not express GRIN2C (14) vs lines expressing it (36) | 1.64× lower at baseline in the lines without GRIN2C | 0.058 | ⚠ within organs, on part of the lines; also absent: FDXR, CYFIP2, GDF15; maybe low, not absent |
| [[TOP1]] | B | TOP1 activity lowers ACER2's level | compounds that target TOP1: 3 of 3 raise it (Doxorubicin, Irinotecan, Topotecan) | 100% of the class's compounds vs 5.0% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[UBASH3B]] | B | UBASH3B activity raises ACER2's level | lines that do not express UBASH3B (7) vs lines expressing it (43) | 1.69× lower at baseline in the lines without UBASH3B | 0.089 | ⚠ within organs, on part of the lines; also absent: ENSG00000284969, CD59, MAMLD1 |
| [[TYMSOS]] | C | TYMSOS activity raises ACER2's level | lines that do not express TYMSOS (3) vs lines expressing it (47) | 2.29× lower at baseline in the lines without TYMSOS | 0.024 | ⚠ few lines (3 vs 47); across organs; co-occurs with SMAD4; also absent: FOXP4-AS1, ENSG00000261341, CCNP; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 062]] — p53 targets up; 78 genes; every member is in the + arm (projection on the module's main direction 0.653). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-15.8, 37.3); signed map (43.5, -24.6). **Vector** length 100.0, 24.5% of its response variance represented; |z| ≥ 3 in 1,304 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | +5.1 | +5.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.6 | +9.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | +4.3 | +8.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~45% of this change | +3.8 | +6.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +3.3 | +7.3 |
|  | [[Amsacrine (drug)]] 5 µM |  | +3.2 | +5.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.0 | +3.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | +8.9 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.7 | +3.9 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -5.5 | -8.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.8 | -5.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -4.4 | -7.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.6 | -7.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -3.3 | -3.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.0 | -1.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -3.0 | -2.7 |
|  | [[venetoclax (drug)]] 5 µM |  | -3.0 | -2.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.9 | -1.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.8 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | alkaline ceramidase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p22.1 — chr9:19,409,009-19,452,505 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ41587, ALKCDase2; previously ASAH3L |
| Gene groups (HGNC) | Alkaline ceramidases |
| Reactome | 3 pathways, smallest: Sphingolipid catabolism; Sphingolipid metabolism; Metabolism of lipids |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5QJU3](https://www.uniprot.org/uniprotkb/Q5QJU3) (Alkaline ceramidase 2):

> Golgi ceramidase that catalyzes the hydrolysis of ceramides into sphingoid bases like sphingosine and free fatty acids at alkaline pH. Ceramides, sphingosine, and its phosphorylated form sphingosine-1-phosphate are bioactive lipids that mediate cellular signaling pathways regulating several biological processes including cell proliferation, apoptosis and differentiation. Has a better catalytic efficiency towards unsaturated long-chain ceramides, including C18:1-, C20:1- and C24:1-ceramides. …

**Summary**, from NCBI Gene [340485](https://www.ncbi.nlm.nih.gov/gene/340485):

> The sphingolipid metabolite sphingosine-1-phosphate promotes cell proliferation and survival, whereas its precursor, sphingosine, has the opposite effect. The ceramidase ACER2 hydrolyzes very long chain ceramides to generate sphingosine (Xu et al., 2006 [PubMed 16940153]).[supplied by OMIM, Jul 2010]

**Accessions** — [HGNC:23675](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23675) · Entrez [340485](https://www.ncbi.nlm.nih.gov/gene/340485) · UniProt [Q5QJU3](https://www.uniprot.org/uniprotkb/Q5QJU3) · Ensembl [ENSG00000177076](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000177076)

## Data

Gene col 10787: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10787); `tables/drug_effects.parquet` (52 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10787, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10787]; `tensor/DDL_lfc|DDL_z.npy` [10787]; `embed/gene_vectors.npy` [10787]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10787 or target_col == 10787). Every well: [[ACER2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. The written part above is `tahoemap/vault_seed/genes/ACER2.md`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
