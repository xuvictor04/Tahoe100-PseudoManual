---
symbol: "ITPR2"
type: "gene"
col: 4401
ensembl_id: "ENSG00000123104"
name: "inositol 1,4,5-trisphosphate receptor type 2"
location: "12p11.23"
module: 183
arm: "+"
pooled_cpm: 241.82
n_lines_expressing: 45
n_dd_up: 12
n_dd_down: 16
n_dd_up_clean: 11
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 5
direction_downstream: 7
tags: ["gene", "module/183"]
generated_by: "tahoemap"
---

# ITPR2

*inositol 1,4,5-trisphosphate receptor type 2* — 12p11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.74× (z +13.2, q 7e-37, up in 31 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (5 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 0.399× (z -14.9, q 0e+00, down in 41 of 42 measured lines) ⚠ toxic. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.581× (z -9.2, q 8e-18, down in 31 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ITPR2-AS1]] (+0.64, fdr 7e-06, ⚠ read-through risk), [[DOCK1]] (+0.53, fdr 4e-05), [[FER]] (+0.51, fdr 2e-05), [[COL27A1]] (+0.50, fdr 1e-05); moves opposite to [[FRG1DP]] (-0.53, fdr 4e-05), [[USPL1]] (-0.52, fdr 1e-05), [[CAPN1-AS1]] (-0.49, fdr 4e-05).
> It is in [[Module 183]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 7 go from it, the strongest it → [[RFX3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 1 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4401.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.74×** | +13.2 | 7e-37 | 31/43 (A-172, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.43×** | +8.6 | 3e-15 | 27/44 (LoVo, NCI-H460, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.62×** | +8.2 | 5e-14 | 26/43 (A-172, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.30×** | +6.2 | 1e-07 | 23/43 (A-172, SNU-1, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.45×** | +6.1 | 1e-07 | 30/42 (SW480, HOP62, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.35×** | +4.9 | 1e-04 | 22/43 (A-172, NCI-H460, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.22×** | +4.7 | 3e-04 | 23/43 (LoVo, A-172, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.31×** | +4.5 | 5e-04 | 23/43 (J82, LoVo, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.35×** | +4.3 | 0.001 | 24/43 (J82, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | **1.25×** | +3.7 | 0.011 | 18/43 (J82, LoVo, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.22×** | +3.4 | 0.033 | 22/42 (SW480, HOP62, …) | rises with dose |  |
| [[Esmolol (hydrochloride) (drug)]] 5 µM |  | **1.22×** | +3.3 | 0.044 | 22/43 (C32, NCI-H1792, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 1.21× | +3.0 | 0.10 | 19/43 (SW480, SW 1088, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 7 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4401.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.399×** | -14.9 | 0e+00 | 41/42 (RKO, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.484×** | -12.3 | 4e-32 | 36/43 (PANC-1, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.581×** | -9.2 | 8e-18 | 31/43 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.583×** | -9.1 | 9e-18 | 31/43 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.400×** | -8.1 | 6e-14 | 36/43 (RKO, LOX-IMVI, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.665×** | -6.9 | 5e-10 | 28/43 (HepG2/C3A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.533×** | -5.6 | 2e-06 | 28/44 (RKO, LS 180, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.540×** | -5.4 | 4e-06 | 22/33 (LOX-IMVI, SW 900, …) | top dose only | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.734×** | -5.2 | 1e-05 | 26/43 (HepG2/C3A, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.762×** | -4.6 | 2e-04 | 26/43 (NCI-H460, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~10% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.767×** | -4.3 | 8e-04 | 23/42 (HepG2/C3A, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.797×** | -3.8 | 0.006 | 21/43 (A-427, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.818×** | -3.4 | 0.029 | 20/43 (C32, PANC-1, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.820×** | -3.4 | 0.033 | 22/43 (HepG2/C3A, AN3 CA, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.876× | -3.2 | 0.055 | 17/43 (RKO, NCI-H23, …) | top dose only | low cells (technical?) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **0.833×** | -3.1 | 0.070 | 21/43 (HS-578T, LOX-IMVI, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4401. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 132 | 16 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.88× (z +33.8) | — |
| [[HepG2_C3A (line)]] | wt | 567 | 0 | 16 (5 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.174× (z -14.4) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.193× (z -14.1) |
| [[SW480 (line)]] | alt | 511 | 14 (1 ⚠) | 2 (2 ⚠) | [[Cobimetinib (drug)]] 5 µM 10.7× (z +18.5) | [[Digitoxin (drug)]] 5 µM 0.303× (z -9.7) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 448 | 0 | 12 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.264× (z -11.5) ⚠ toxic · without an alert: [[Vinblastine (sulfate) (drug)]] 5 µM 0.405× (z -11.5) |
| [[NCI-H460 (line)]] | wt | 144 | 2 | 10 (6 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.60× (z +18.6) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.309× (z -16.2) |
| [[PANC-1 (line)]] | alt | 455 | 0 | 12 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.241× (z -19.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.258× (z -18.8) |
| [[NCI-H23 (line)]] | alt | 936 | 0 | 11 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.210× (z -20.5) |
| [[LoVo (line)]] | wt | 190 | 8 (2 ⚠) | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.58× (z +24.2) | [[Digitoxin (drug)]] 5 µM 0.456× (z -10.5) ⚠ toxic; transcription drop · without an alert: [[PH-797804 (drug)]] 5 µM 0.282× (z -8.9) |
| [[J82 (line)]] | alt | 187 | 7 (2 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.08× (z +18.9) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.452× (z -9.4) |
| [[RKO (line)]] | wt | 411 | 0 | 9 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.172× (z -19.3) ⚠ toxic · without an alert: [[PH-797804 (drug)]] 5 µM 0.0697× (z -15.8) |
| [[SW 900 (line)]] | alt | 199 | 4 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.40× (z +19.7) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.362× (z -11.2) ⚠ toxic · without an alert: [[PH-797804 (drug)]] 5 µM 0.227× (z -8.8) |
| [[LOX-IMVI (line)]] | wt | 372 | 0 | 6 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.316× (z -13.4) ⚠ toxic · without an alert: [[PH-797804 (drug)]] 5 µM 0.147× (z -12.1) |
| [[NCI-H1573 (line)]] | alt | 232 | 0 | 6 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.183× (z -17.5) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.227× (z -16.0) |
| [[C32 (line)]] | wt | 591 | 0 | 5 (1 ⚠) | — | [[Ponatinib (drug)]] 5 µM 0.254× (z -10.6) |
| [[HOP62 (line)]] | alt | 300 | 1 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.76× (z +15.5) | [[Digitoxin (drug)]] 5 µM 0.328× (z -12.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.382× (z -10.4) |
| [[MIA PaCa-2 (line)]] | alt | 153 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +11.0) | [[Adagrasib (drug)]] 0.05 µM 0.554× (z -18.1) ⚠ position not correctable |
| [[NCI-H1792 (line)]] | alt | 308 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.229× (z -19.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.355× (z -13.4) |
| [[H4 (line)]] | wt | 186 | 2 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.36× (z +11.7) | [[Digitoxin (drug)]] 5 µM 0.285× (z -12.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.405× (z -8.7) |
| [[hTERT-HPNE (line)]] | wt | 276 | 1 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +13.4) | [[Digitoxin (drug)]] 5 µM 0.253× (z -13.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.412× (z -8.8) |
| [[A-427 (line)]] | wt | 164 | 1 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.05× (z +9.3) | [[Ixazomib citrate (drug)]] 5 µM 0.463× (z -10.0) |
| [[HEC-1-A (line)]] | alt | 71.3 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.05× (z +9.7) | — |
| [[HT-29 (line)]] | alt | 285 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +16.6) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.275× (z -14.2) ⚠ toxic · without an alert: [[Vinblastine (sulfate) (drug)]] 5 µM 0.542× (z -9.9) |
| [[KATO III (line)]] | alt | 156 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.323× (z -12.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.370× (z -11.1) |
| [[SNU-1 (line)]] | wt | 185 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +8.9) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.303× (z -11.1) ⚠ toxic |
| [[A498 (line)]] | wt | 162 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.81× (z +10.1) | — |
| [[AN3 CA (line)]] | alt | 201 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.154× (z -14.3) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.317× (z -9.5) |
| [[COLO 205 (line)]] | alt | 153 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.89× (z +9.6) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.303× (z -12.2) ⚠ toxic |
| [[HS-578T (line)]] | alt | 359 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.317× (z -10.0) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 115 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.42× (z +22.5) | — |
| [[RPMI-7951 (line)]] | alt | 128 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +11.4) | — |
| [[SNU-423 (line)]] | alt | 209 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +10.2) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.335× (z -11.5) ⚠ toxic |
| [[A549 (line)]] | wt | 155 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.386× (z -9.3) |
| [[BT-474 (line)]] | alt | 130 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.72× (z +17.6) | — |
| [[CHP-212 (line)]] | wt | 219 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.144× (z -11.2) ⚠ toxic |
| [[HCT15 (line)]] | alt | 156 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.85× (z +9.2) | — |
| [[Hs 766T (line)]] | wt | 158 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.342× (z -9.9) ⚠ toxic |
| [[NCI-H596 (line)]] | alt | 254 | 1 (1 ⚠) | 0 | [[Trametinib (drug)]] 5 µM 7.10× (z +9.5) ⚠ cell-cycle shift, explains ~7% of this change | — |
| [[SHP-77 (line)]] | alt | 268 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.65× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[SW 1271 (line)]] | alt | 323 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.221× (z -8.8) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 57.8 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 50.8 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 20.6 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 166 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 189 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 31.8 n.m. | — | — | — | — |
| [[NCI-H661 (line)]] | alt | 139 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 223 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 97.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 49.1 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 76.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4401), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*42 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ITPR2-AS1]] | +0.64 | +0.70 / +0.60 | both halves | 7e-06 | ⚠ **readthrough risk**: ITPR2-AS1 lies 0.0 kb 3′ of this gene on the same strand (can correlate by spillover, not regulation) |
| [[DOCK1]] | +0.53 | +0.42 / +0.49 | both halves | 4e-05 | pathway: Fcgamma receptor (FCGR) dependent phagocytosis |
| [[FER]] | +0.51 | +0.47 / +0.49 | both halves | 2e-05 |  |
| [[COL27A1]] | +0.50 | +0.49 / +0.49 | both halves | 1e-05 |  |
| [[DSE]] | +0.47 | +0.55 / +0.43 | both halves | 3e-05 |  |
| [[SIPA1L1]] | +0.47 | +0.42 / +0.50 | both halves | 4e-05 |  |
| [[SLIT2]] | +0.47 | +0.54 / +0.42 | both halves | 4e-05 |  |
| [[MYO10]] | +0.46 | +0.41 / +0.48 | both halves | 4e-05 | pathway: Fcgamma receptor (FCGR) dependent phagocytosis |
| [[NAV3]] | +0.46 | +0.41 / +0.46 | both halves | 4e-05 |  |
| [[IMMP2L]] | +0.45 | +0.46 / +0.44 | both halves | 3e-05 |  |
| [[CALCRL-AS1]] | +0.45 | +0.58 / +0.34 | both halves | 1e-04 |  |
| [[NEK10]] | +0.45 | +0.47 / +0.43 | both halves | 3e-05 |  |
| [[WWC2]] | +0.45 | +0.32 / +0.45 | both halves | 2e-04 |  |

## Genes that move opposite

*58 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FRG1DP]] | -0.53 | -0.42 / -0.53 | both halves | 4e-05 |  |
| [[USPL1]] | -0.52 | -0.56 / -0.50 | both halves | 1e-05 |  |
| [[CAPN1-AS1]] | -0.49 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[DUSP11]] | -0.49 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[LRIG2]] | -0.48 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[PRUNE1]] | -0.47 | -0.42 / -0.45 | both halves | 4e-05 |  |
| [[PSMF1]] | -0.46 | -0.51 / -0.39 | both halves | 5e-05 |  |
| [[ZNF836]] | -0.46 | -0.41 / -0.40 | both halves | 5e-05 |  |
| [[CDADC1]] | -0.46 | -0.44 / -0.40 | both halves | 4e-05 |  |
| [[SDHAP4]] | -0.46 | -0.55 / -0.39 | both halves | 6e-05 |  |
| [[EID2B]] | -0.46 | -0.30 / -0.45 | both halves | 2e-04 |  |
| [[ALG9]] | -0.45 | -0.53 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 3, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ITPR2's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[LINC03041]] | B | LINC03041 activity raises ITPR2's level | lines that do not express LINC03041 (18) vs lines expressing it (32) | 1.54× lower at baseline in the lines without LINC03041 | 0.069 | ⚠ within organs, on part of the lines; also absent: BNC2, HECW2, ACTN2; maybe low, not absent |
| [[CFAP299]] | B | CFAP299 activity raises ITPR2's level | lines that do not express CFAP299 (27) vs lines expressing it (23) | 1.56× lower at baseline in the lines without CFAP299 | 0.090 | ⚠ within organs, on part of the lines; also absent: FGF5, LINC00702, JAM2 |
| [[ITPR2-AS1]] | C | ITPR2-AS1 activity raises ITPR2's level | lines that do not express ITPR2-AS1 (4) vs lines expressing it (46) | 5.53× lower at baseline in the lines without ITPR2-AS1 | 0.002 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ITPR2, ENSG00000286162, SPATA17; co-absent with the target |
| [[NEK10]] | C | NEK10 activity raises ITPR2's level | lines that do not express NEK10 (6) vs lines expressing it (44) | 3.03× lower at baseline in the lines without NEK10 | 0.066 | ⚠ within organs, on part of the lines; also absent: ZNF474, ITPR2-AS1, LINC00334; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 5, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RFX3]] | B | ITPR2 activity raises RFX3's level | lines that do not express ITPR2 (5) vs lines expressing it (45) | 1.86× lower at baseline in the lines without ITPR2 | 0.006 | ⚠ within organs, on part of the lines; also absent: ITPR2-AS1, ENSG00000286162, SPATA17; maybe low, not absent |
| [[ZNF594-DT]] | B | ITPR2 activity raises ZNF594-DT's level | lines that do not express ITPR2 (5) vs lines expressing it (45) | 1.68× lower at baseline in the lines without ITPR2 | 0.088 | ⚠ within organs, on part of the lines; also absent: ITPR2-AS1, ENSG00000286162, SPATA17; maybe low, not absent |
| [[FBXL17]] | B | ITPR2 activity raises FBXL17's level | lines that do not express ITPR2 (5) vs lines expressing it (45) | 1.43× lower at baseline in the lines without ITPR2 | 0.091 | ⚠ within organs, on part of the lines; also absent: ITPR2-AS1, ENSG00000286162, SPATA17; maybe low, not absent |
| [[STARD13]] | B | ITPR2 activity raises STARD13's level | lines that do not express ITPR2 (5) vs lines expressing it (45) | 3.59× lower at baseline in the lines without ITPR2 | 0.098 | ⚠ within organs, on part of the lines; also absent: ITPR2-AS1, ENSG00000286162, SPATA17; maybe low, not absent |
| [[SMYD4]] | B | ITPR2 activity raises SMYD4's level | lines that do not express ITPR2 (5) vs lines expressing it (45) | 1.43× lower at baseline in the lines without ITPR2 | 0.098 | ⚠ within organs, on part of the lines; also absent: ITPR2-AS1, ENSG00000286162, SPATA17; maybe low, not absent |
| [[ITPR2-AS1]] | C | ITPR2 activity raises ITPR2-AS1's level | lines that do not express ITPR2 (5) vs lines expressing it (45) | 2.49× lower at baseline in the lines without ITPR2 | 0.032 | ⚠ within organs, on part of the lines; also absent: ITPR2-AS1, ENSG00000286162, SPATA17; maybe low, not absent; co-absent with the target |
| [[NEK10]] | C | ITPR2 activity raises NEK10's level | lines that do not express ITPR2 (5) vs lines expressing it (45) | 2.91× lower at baseline in the lines without ITPR2 | 0.0999 | ⚠ within organs, on part of the lines; also absent: ITPR2-AS1, ENSG00000286162, SPATA17; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 183]]; 21 genes; every member is in the + arm (projection on the module's main direction -0.518). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.32; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-2.6, -15.6); signed map (14.5, 21.0). **Vector** length 118, 37.7% of its response variance represented; |z| ≥ 3 in 1,564 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +9.4 | +13.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.1 | +1.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.2 | +2.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.8 | +8.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.5 | +6.1 |
|  | [[Busulfan (drug)]] 5 µM |  | +2.7 | +2.1 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.6 | +0.2 |
|  | [[Thymol (drug)]] 5 µM |  | +2.3 | +2.1 |
|  | [[Busulfan (drug)]] 0.05 µM |  | +2.2 | +2.1 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -11.0 | -14.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -6.8 | -5.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.3 | -3.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | -4.8 | -2.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.8 | -8.1 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.3 | -2.5 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -2.7 | -0.9 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.6 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | inositol 1,4,5-trisphosphate receptor type 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p11.23 — chr12:26,335,352-26,833,194 (-) |
| Ensembl biotype | protein_coding |
| Also known as | IP3R2, CFAP48 |
| Gene groups (HGNC) | Inositol 1,4,5-triphosphate receptors; Cilia and flagella associated |
| Hallmark sets | PI3K_AKT_MTOR_SIGNALING |
| Reactome | 45 pathways, smallest: Elevation of cytosolic Ca2+ levels; Rituximab:MS4A1 (rituximab:CD20) targets B cells for antibody-dependent cellular cytotoxicity by NK cells; CLEC7A (Dectin-1) induces NFAT activation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14571](https://www.uniprot.org/uniprotkb/Q14571) (Inositol 1,4,5-trisphosphate-gated calcium channel ITPR2):

> Inositol 1,4,5-trisphosphate-gated calcium channel that upon inositol 1,4,5-trisphosphate binding transports calcium from the endoplasmic reticulum lumen to cytoplasm. Exists in two states; a long-lived closed state where the channel is essentially 'parked' with only very rare visits to an open state and that ligands facilitate the transition from the 'parked' state into a 'drive' mode represented by periods of bursting activity (By similarity).

**Summary**, from NCBI Gene [3709](https://www.ncbi.nlm.nih.gov/gene/3709):

> The protein encoded by this gene belongs to the inositol 1,4,5-triphosphate receptor family, whose members are second messenger intracellular calcium release channels. These proteins mediate a rise in cytoplasmic calcium in response to receptor activated production of inositol triphosphate. Inositol triphosphate receptor-mediated signaling is involved in many processes including cell migration, cell division, smooth muscle contraction, and neuronal signaling. This protein is a type 2 receptor …

**Accessions** — [HGNC:6181](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6181) · Entrez [3709](https://www.ncbi.nlm.nih.gov/gene/3709) · UniProt [Q14571](https://www.uniprot.org/uniprotkb/Q14571) · Ensembl [ENSG00000123104](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000123104)

## Data

Gene col 4401: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4401); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4401, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4401]; `tensor/DDL_lfc|DDL_z.npy` [4401]; `embed/gene_vectors.npy` [4401]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4401 or target_col == 4401). Every well: [[ITPR2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ITPR2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
