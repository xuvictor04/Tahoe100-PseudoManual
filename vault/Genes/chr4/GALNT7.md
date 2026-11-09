---
symbol: "GALNT7"
type: "gene"
col: 3063
ensembl_id: "ENSG00000109586"
name: "polypeptide N-acetylgalactosaminyltransferase 7"
location: "4q34.1"
module: 25
arm: "+"
pooled_cpm: 103.96
n_lines_expressing: 47
n_dd_up: 13
n_dd_down: 10
n_dd_up_clean: 9
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 1
direction_downstream: 4
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# GALNT7

*polypeptide N-acetylgalactosaminyltransferase 7* — 4q34.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.70× (z +18.2, q 0e+00, up in 37 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.398× (z -22.4, q 0e+00, down in 42 of 45 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GPD2]] (+0.63, fdr 1e-05), [[PTPRK]] (+0.60, fdr 1e-05), [[MBNL3]] (+0.60, fdr 5e-05); moves opposite to [[ATG4B]] (-0.67, fdr 1e-05), [[ZNF473]] (-0.61, fdr 1e-05), [[VRK3]] (-0.60, fdr 1e-05).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); 4 go from it, the strongest it → [[PLCL2]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 8 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3063.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.70×** | +18.2 | 0e+00 | 37/46 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.83×** | +14.7 | 0e+00 | 29/46 (HOP62, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.59×** | +10.8 | 7e-25 | 35/45 (RKO, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.52×** | +9.7 | 3e-20 | 29/45 (A549, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.51×** | +9.6 | 7e-20 | 25/39 (PANC-1, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.49×** | +8.9 | 4e-17 | 23/42 (HOP62, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.40×** | +7.9 | 2e-13 | 31/47 (RKO, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.33×** | +7.0 | 2e-10 | 26/45 (NCI-H460, HOP62, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.31×** | +6.6 | 2e-09 | 28/45 (LoVo, CFPAC-1, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.29×** | +6.3 | 2e-08 | 25/45 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.26×** | +5.7 | 7e-07 | 23/45 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +5.4 | 3e-06 | 20/45 (CFPAC-1, PANC-1, …) | rises with dose | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.16× | +5.0 | 2e-05 | 16/45 (A-427, HOP62, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 1.20× | +4.2 | 0.001 | 19/44 (NCI-H460, HOP62, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~5% of this change | 1.12× | +4.0 | 0.003 | 12/45 (SW1417, A549, …) | all doses, stronger at high dose | low cells (technical?) |
| [[venetoclax (drug)]] 5 µM |  | **1.34×** | +3.7 | 0.008 | 19/45 (AsPC-1, RKO, …) | rises with dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 1.11× | +3.5 | 0.016 | 8/45 (SW480, Panc 03.27, …) | all doses, flat |  |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | 1.14× | +3.3 | 0.035 | 9/45 (hTERT-HPNE, C32, …) | inconsistent across doses | low cells (technical?) |
| [[Cobimetinib (drug)]] 5 µM |  | 1.14× | +3.1 | 0.051 | 15/44 (SW480, HOP62, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **1.28×** | +3.1 | 0.053 | 16/45 (CFPAC-1, NCI-H1573, …) | top dose only | noisy plate (z scaled) |
| [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | 1.14× | +2.9 | 0.083 | 5/46 (SW480, C32, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.09× | +2.9 | 0.088 | 7/46 (SW480, Panc 03.27, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 2 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3063.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.398×** | -22.4 | 0e+00 | 42/45 (KATO III, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.445×** | -19.6 | 0e+00 | 42/45 (Panc 03.27, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.591×** | -12.8 | 4e-35 | 37/45 (SW480, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.630×** | -11.2 | 5e-27 | 38/45 (Panc 03.27, LoVo, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.795×** | -5.6 | 3e-06 | 25/45 (NCI-H1573, A498, …) | two highest doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.803×** | -5.0 | 5e-05 | 25/45 (Panc 03.27, BT-474, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~3% of this change | **0.829×** | -4.5 | 4e-04 | 22/45 (SW1417, HT-29, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.818×** | -4.5 | 5e-04 | 17/44 (CHP-212, NCI-H2347, …) | inconsistent across doses | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~6% of this change | 0.838× | -4.3 | 0.001 | 20/45 (KATO III, Panc 03.27, …) | two highest doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.802×** | -3.6 | 0.019 | 15/45 (SW 1271, COLO 205, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.764×** | -3.4 | 0.033 | 14/46 (RKO, Panc 03.27, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 0.871× | -3.3 | 0.040 | 18/45 (NCI-H1573, A498, …) | inconsistent across doses |  |
| [[Budesonide (drug)]] 0.5 µM |  | 0.881× | -3.1 | 0.091 | 16/45 (NCI-H1573, A498, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | 0.831× | -3.0 | 0.10 | 13/45 (HS-578T, NCI-H1792, …) | rises with dose | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3063. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 74.8 | 7 (3 ⚠) | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.88× (z +21.5) | [[Panobinostat (drug)]] 5 µM 0.460× (z -11.2) |
| [[PANC-1 (line)]] | alt | 152 | 6 (4 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.31× (z +12.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.08× (z +11.2) | [[Panobinostat (drug)]] 5 µM 0.301× (z -18.5) |
| [[HOP62 (line)]] | alt | 75.3 | 6 (3 ⚠) | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.57× (z +16.2) | [[Panobinostat (drug)]] 5 µM 0.412× (z -10.8) |
| [[LOX-IMVI (line)]] | wt | 53.7 | 3 (2 ⚠) | 4 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.41× (z +14.2) | [[Homoharringtonine (drug)]] 5 µM 0.455× (z -12.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.386× (z -10.8) |
| [[RKO (line)]] | wt | 89.7 | 4 (1 ⚠) | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.50× (z +14.9) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.284× (z -14.0) ⚠ toxic; cell-cycle shift, explains ~43% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.427× (z -9.8) |
| [[LoVo (line)]] | wt | 175 | 2 (1 ⚠) | 4 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.67× (z +9.7) | [[Panobinostat (drug)]] 5 µM 0.225× (z -20.2) |
| [[Panc 03.27 (line)]] | alt | 195 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.166× (z -22.8) |
| [[A549 (line)]] | wt | 87.0 | 2 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 2.47× (z +10.5) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 2.33× (z +9.9) | [[Panobinostat (drug)]] 5 µM 0.284× (z -15.3) |
| [[HT-29 (line)]] | alt | 130 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.228× (z -18.0) |
| [[KATO III (line)]] | alt | 210 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.178× (z -21.3) |
| [[LS 180 (line)]] | wt | 127 | 2 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.02× (z +10.9) | [[Panobinostat (drug)]] 0.5 µM 0.328× (z -12.3) |
| [[NCI-H23 (line)]] | alt | 36.9 | 3 (1 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.79× (z +12.6) | [[Panobinostat (drug)]] 5 µM 0.282× (z -11.0) |
| [[NCI-H2347 (line)]] | alt | 172 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.362× (z -15.8) |
| [[SW1417 (line)]] | alt | 112 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.270× (z -17.3) |
| [[SW480 (line)]] | alt | 173 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.148× (z -21.8) |
| [[A498 (line)]] | wt | 169 | 1 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 1.66× (z +8.8) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 5 µM 0.374× (z -12.1) |
| [[BT-474 (line)]] | alt | 205 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.237× (z -12.2) |
| [[C32 (line)]] | wt | 127 | 2 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.69× (z +10.7) ⚠ toxic; transcription drop · without an alert: [[PH-797804 (drug)]] 5 µM 4.72× (z +9.1) | [[Auranofin (drug)]] 5 µM 0.454× (z -8.9) |
| [[CFPAC-1 (line)]] | alt | 83.0 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.46× (z +18.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.91× (z +9.7) | — |
| [[COLO 205 (line)]] | alt | 156 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -15.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.312× (z -10.3) |
| [[NCI-H2030 (line)]] | alt | 83.5 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.79× (z +10.3) | [[Panobinostat (drug)]] 0.5 µM 0.479× (z -9.1) |
| [[SHP-77 (line)]] | alt | 107 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.269× (z -13.5) |
| [[A-172 (line)]] | wt | 77.1 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.376× (z -10.9) |
| [[AsPC-1 (line)]] | alt | 77.3 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.11× (z +10.2) | [[Panobinostat (drug)]] 0.5 µM 0.348× (z -10.4) |
| [[C-33 A (line)]] | alt | 68.3 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.27× (z +9.9) | — |
| [[HEC-1-A (line)]] | alt | 64.2 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.20× (z +12.9) | — |
| [[Hs 766T (line)]] | wt | 48.7 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.274× (z -10.6) |
| [[HS-578T (line)]] | alt | 65.0 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.361× (z -10.9) |
| [[NCI-H1573 (line)]] | alt | 86.1 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.24× (z +8.6) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.418× (z -9.3) |
| [[SNU-423 (line)]] | alt | 93.4 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.260× (z -15.0) |
| [[A-427 (line)]] | wt | 44.4 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.334× (z -10.6) |
| [[HCT15 (line)]] | alt | 64.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.45× (z +8.5) | — |
| [[hTERT-HPNE (line)]] | wt | 71.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.68× (z +13.0) | — |
| [[J82 (line)]] | alt | 52.0 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.409× (z -8.8) |
| [[RPMI-7951 (line)]] | alt | 36.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.56× (z +13.4) | — |
| [[SK-MEL-2 (line)]] | alt | 84.1 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.420× (z -9.5) |
| [[SW 900 (line)]] | alt | 86.2 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.395× (z -9.4) |
| [[SW48 (line)]] | wt | 103 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.259× (z -12.0) |
| [[AN3 CA (line)]] | alt | 116 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 73.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 101 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 13.7 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 23.3 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 71.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 90.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.2 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 51.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 60.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 68.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3063), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*49 of its nearest partners move with it, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPD2]] | +0.63 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[PTPRK]] | +0.60 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[MBNL3]] | +0.60 | +0.54 / +0.39 | both halves | 5e-05 |  |
| [[SEPTIN11]] | +0.59 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[SLC12A2-DT]] | +0.59 | +0.48 / +0.39 | both halves | 6e-05 |  |
| [[ERAP1]] | +0.58 | +0.41 / +0.48 | both halves | 4e-05 |  |
| [[PLCL2]] | +0.57 | +0.57 / +0.35 | both halves | 1e-04 | same gene group |
| [[VSIG10]] | +0.56 | +0.51 / +0.34 | both halves | 1e-04 |  |
| [[STK26]] | +0.56 | +0.41 / +0.51 | both halves | 4e-05 |  |
| [[OGFRL1]] | +0.56 | +0.37 / +0.48 | both halves | 8e-05 |  |
| [[GALNT7-DT]] | +0.56 | +0.41 / +0.31 | both halves | 2e-04 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[CABLES1]] | +0.56 | +0.48 / +0.37 | both halves | 8e-05 |  |
| [[ATP11C]] | +0.56 | +0.42 / +0.45 | both halves | 4e-05 | same gene group |

## Genes that move opposite

*51 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATG4B]] | -0.67 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[ZNF473]] | -0.61 | -0.54 / -0.51 | both halves | 1e-05 |  |
| [[VRK3]] | -0.60 | -0.49 / -0.53 | both halves | 1e-05 |  |
| [[MT1X]] | -0.60 | -0.46 / -0.51 | both halves | 3e-05 |  |
| [[RGP1]] | -0.59 | -0.50 / -0.54 | both halves | 1e-05 |  |
| [[MRGBP]] | -0.58 | -0.41 / -0.54 | both halves | 4e-05 |  |
| [[NOSIP]] | -0.58 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[PBX4]] | -0.57 | -0.44 / -0.37 | both halves | 9e-05 |  |
| [[RBAK-RBAKDN]] | -0.57 | -0.41 / -0.53 | both halves | 4e-05 |  |
| [[CLTCL1]] | -0.56 | -0.45 / -0.38 | both halves | 6e-05 |  |
| [[ASL]] | -0.56 | -0.46 / -0.36 | both halves | 9e-05 |  |
| [[GP6-AS1]] | -0.56 | -0.53 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers GALNT7's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 0, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLCL2]] | C | GALNT7 activity raises PLCL2's level | lines that do not express GALNT7 (3) vs lines expressing it (47) | 5.70× lower at baseline in the lines without GALNT7 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: RND3, SCML1, TTC39C; its own permutation p |
| [[PTPRK]] | C | GALNT7 activity raises PTPRK's level | lines that do not express GALNT7 (3) vs lines expressing it (47) | 3.07× lower at baseline in the lines without GALNT7 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: RND3, SCML1, TTC39C; its own permutation p |
| [[ERAP1]] | C | GALNT7 activity raises ERAP1's level | lines that do not express GALNT7 (3) vs lines expressing it (47) | 1.42× lower at baseline in the lines without GALNT7 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: RND3, SCML1, TTC39C; its own permutation p |
| [[GALNT7-DT]] | C | GALNT7 activity raises GALNT7-DT's level | lines that do not express GALNT7 (3) vs lines expressing it (47) | 3.02× lower at baseline in the lines without GALNT7 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: RND3, SCML1, TTC39C; co-absent with the target |

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.342). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-10.9, 11.2); signed map (25.6, -34.4). **Vector** length 138, 42.2% of its response variance represented; |z| ≥ 3 in 1,297 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +10.9 | +18.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +7.6 | +10.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +6.5 | +7.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.3 | +14.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | +4.8 | +4.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.3 | +5.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +3.7 | +2.6 |
|  | [[Trametinib (drug)]] 0.05 µM |  | +3.6 | +3.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.5 | +2.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.4 | +2.6 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -9.6 | -22.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -9.4 | -11.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | -9.3 | -19.6 |
|  | [[Belinostat (drug)]] 5 µM |  | -6.4 | -12.8 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -5.6 | -5.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.2 | -5.6 |
|  | [[Budesonide (drug)]] 0.5 µM |  | -3.4 | -3.1 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -3.0 | -3.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.8 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | polypeptide N-acetylgalactosaminyltransferase 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q34.1 — chr4:173,168,811-173,323,967 (+) |
| Ensembl biotype | protein_coding |
| Also known as | GALNAC-T7 |
| Gene groups (HGNC) | Polypeptide N-acetylgalactosaminyltransferases; MicroRNA protein coding host genes |
| Reactome | 2 pathways, smallest: O-linked glycosylation of mucins; O-linked glycosylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86SF2](https://www.uniprot.org/uniprotkb/Q86SF2) (N-acetylgalactosaminyltransferase 7):

> Glycopeptide transferase involved in O-linked oligosaccharide biosynthesis, which catalyzes the transfer of an N-acetyl-D-galactosamine residue to an already glycosylated peptide. In contrast to other proteins of the family, it does not act as a peptide transferase that transfers GalNAc onto serine or threonine residue on the protein receptor, but instead requires the prior addition of a GalNAc on a peptide before adding additional GalNAc moieties. Some peptide transferase activity is however …

**Summary**, from NCBI Gene [51809](https://www.ncbi.nlm.nih.gov/gene/51809):

> This gene encodes GalNAc transferase 7, a member of the GalNAc-transferase family. The enzyme encoded by this gene controls the initiation step of mucin-type O-linked protein glycosylation and transfer of N-acetylgalactosamine to serine and threonine amino acid residues. This enzyme is a type II transmembrane protein and shares common sequence motifs with other family members. Unlike other family members, this enzyme shows exclusive specificity for partially GalNAc-glycosylated acceptor …

**Accessions** — [HGNC:4129](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4129) · Entrez [51809](https://www.ncbi.nlm.nih.gov/gene/51809) · UniProt [Q86SF2](https://www.uniprot.org/uniprotkb/Q86SF2) · Ensembl [ENSG00000109586](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000109586)

## Data

Gene col 3063: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3063); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3063, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3063]; `tensor/DDL_lfc|DDL_z.npy` [3063]; `embed/gene_vectors.npy` [3063]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3063 or target_col == 3063). Every well: [[GALNT7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GALNT7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
