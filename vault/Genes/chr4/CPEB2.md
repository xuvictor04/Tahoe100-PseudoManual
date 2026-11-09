---
symbol: "CPEB2"
type: "gene"
col: 6014
ensembl_id: "ENSG00000137449"
name: "cytoplasmic polyadenylation element binding protein 2"
location: "4p15.32"
module: 68
arm: "+"
pooled_cpm: 99.53
n_lines_expressing: 47
n_dd_up: 23
n_dd_down: 12
n_dd_up_clean: 18
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 5
direction_downstream: 3
tags: ["gene", "module/068"]
generated_by: "tahoemap"
---

# CPEB2

*cytoplasmic polyadenylation element binding protein 2* — 4p15.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.63× (z +28.0, q 0e+00, up in 44 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.309× (z -18.0, q 0e+00, down in 41 of 45 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC00882]] (+0.68, fdr 1e-05), [[CAMK2D]] (+0.68, fdr 1e-05), [[PATL2]] (+0.64, fdr 3e-05); moves opposite to [[INTS4]] (-0.63, fdr 1e-05), [[STARD3]] (-0.58, fdr 3e-05), [[ERI3]] (-0.58, fdr 5e-05).
> It sits in the **+** arm of [[Module 068]].
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[MSC]] → it (grade B ⚠); 3 go from it, the strongest it → [[GUCY2C-AS1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 6 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6014.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.63×** | +28.0 | 0e+00 | 44/45 (A549, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.33×** | +18.4 | 0e+00 | 43/45 (A549, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 5 µM |  | **3.34×** | +17.8 | 0e+00 | 45/45 (A549, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.89×** | +8.5 | 2e-15 | 38/46 (LoVo, Hs 766T, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.62×** | +7.4 | 2e-11 | 32/45 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.64×** | +7.3 | 2e-11 | 29/44 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.61×** | +7.3 | 2e-11 | 31/45 (NCI-H460, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.61×** | +7.3 | 2e-11 | 34/45 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.60×** | +7.2 | 3e-11 | 33/45 (NCI-H460, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.47×** | +5.9 | 2e-07 | 27/45 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.95×** | +5.4 | 4e-06 | 27/45 (LoVo, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.36×** | +4.6 | 2e-04 | 28/44 (NCI-H460, HOP62, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.31×** | +4.1 | 0.002 | 27/44 (H4, HOP62, …) | rises with dose | low cells (technical?) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.28×** | +3.8 | 0.007 | 21/45 (Hs 766T, CFPAC-1, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.28×** | +3.7 | 0.009 | 22/47 (NCI-H460, A549, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.24×** | +3.3 | 0.033 | 22/44 (NCI-H460, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[EX229 (drug)]] 5 µM |  | **1.50×** | +3.3 | 0.035 | 18/45 (Hs 766T, SHP-77, …) | top dose only | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.24×** | +3.2 | 0.047 | 17/44 (NCI-H460, SK-MEL-2, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.23×** | +3.1 | 0.052 | 20/45 (NCI-H460, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.22×** | +3.0 | 0.069 | 22/45 (NCI-H460, A549, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 6 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6014.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.309×** | -18.0 | 0e+00 | 41/45 (NCI-H2347, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.361×** | -15.6 | 0e+00 | 40/45 (NCI-H2347, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.371×** | -15.2 | 0e+00 | 39/45 (NCI-H2347, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **0.521×** | -10.0 | 2e-21 | 33/45 (A-172, NCI-H2347, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **0.509×** | -10.0 | 2e-21 | 36/40 (A-427, NCI-H2347, …) | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.796×** | -4.9 | 7e-05 | 24/45 (NCI-H2347, LOX-IMVI, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~43% of this change | **0.732×** | -4.6 | 3e-04 | 25/44 (CFPAC-1, LOX-IMVI, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.767×** | -4.1 | 0.003 | 24/46 (LoVo, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.767×** | -4.1 | 0.003 | 25/45 (BT-474, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.781×** | -3.8 | 0.008 | 24/45 (H4, LOX-IMVI, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.662×** | -3.3 | 0.048 | 20/42 (NCI-H1573, SW48, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.810×** | -3.2 | 0.058 | 19/45 (J82, A498, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.43 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6014. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 67.4 | 14 (2 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 5.70× (z +20.0) | [[Panobinostat (drug)]] 5 µM 0.347× (z -8.6) |
| [[A-172 (line)]] | wt | 81.3 | 5 | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.15× (z +21.4) | [[Dinaciclib (drug)]] 0.5 µM 0.292× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.329× (z -11.9) |
| [[NCI-H2347 (line)]] | alt | 130 | 4 | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.22× (z +22.5) | [[Panobinostat (drug)]] 5 µM 0.156× (z -20.5) |
| [[SW48 (line)]] | wt | 216 | 5 | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 5.08× (z +12.4) | [[Panobinostat (drug)]] 0.5 µM 0.207× (z -12.1) |
| [[C32 (line)]] | wt | 445 | 2 | 7 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +9.9) | [[Panobinostat (drug)]] 5 µM 0.215× (z -13.0) |
| [[Hs 766T (line)]] | wt | 213 | 6 (2 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 5.83× (z +22.3) | [[Panobinostat (drug)]] 0.5 µM 0.152× (z -16.9) |
| [[NCI-H1573 (line)]] | alt | 258 | 6 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 7.94× (z +24.7) | [[Panobinostat (drug)]] 5 µM 0.303× (z -10.2) |
| [[A549 (line)]] | wt | 80.2 | 6 | 2 | [[Homoharringtonine (drug)]] 5 µM 10.8× (z +32.2) | [[Belinostat (drug)]] 5 µM 0.393× (z -8.9) |
| [[CFPAC-1 (line)]] | alt | 115 | 3 | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.28× (z +25.4) | [[Panobinostat (drug)]] 5 µM 0.350× (z -11.3) |
| [[LoVo (line)]] | wt | 182 | 5 | 3 | [[Homoharringtonine (drug)]] 5 µM 4.56× (z +22.1) | [[Panobinostat (drug)]] 5 µM 0.216× (z -15.8) |
| [[LOX-IMVI (line)]] | wt | 153 | 3 | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.08× (z +17.5) | [[Panobinostat (drug)]] 5 µM 0.237× (z -16.0) |
| [[RPMI-7951 (line)]] | alt | 168 | 2 | 6 (3 ⚠) | [[Harringtonine (drug)]] 5 µM 3.77× (z +11.6) | [[Panobinostat (drug)]] 0.5 µM 0.263× (z -12.2) |
| [[BT-474 (line)]] | alt | 44.9 | 3 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.88× (z +19.5) | [[Panobinostat (drug)]] 0.5 µM 0.164× (z -14.1) |
| [[HS-578T (line)]] | alt | 132 | 3 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.45× (z +19.2) | [[Panobinostat (drug)]] 5 µM 0.194× (z -14.9) |
| [[hTERT-HPNE (line)]] | wt | 162 | 4 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.08× (z +17.2) | [[Panobinostat (drug)]] 5 µM 0.248× (z -10.4) |
| [[NCI-H1792 (line)]] | alt | 94.5 | 3 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +15.6) | [[Panobinostat (drug)]] 5 µM 0.272× (z -13.3) |
| [[Panc 03.27 (line)]] | alt | 70.0 | 3 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.99× (z +22.8) | [[Dinaciclib (drug)]] 5 µM 0.239× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.278× (z -11.5) |
| [[SNU-423 (line)]] | alt | 143 | 2 | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.85× (z +18.1) | [[Panobinostat (drug)]] 5 µM 0.175× (z -16.5) |
| [[SW 900 (line)]] | alt | 171 | 3 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +11.1) | [[Belinostat (drug)]] 5 µM 0.314× (z -9.5) |
| [[SW1417 (line)]] | alt | 44.0 | 3 | 3 | [[Homoharringtonine (drug)]] 5 µM 4.82× (z +20.2) | [[Panobinostat (drug)]] 5 µM 0.274× (z -11.8) |
| [[A498 (line)]] | wt | 201 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 9.32× (z +30.1) | [[Dinaciclib (drug)]] 0.5 µM 0.396× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[HEC-1-A (line)]] | alt | 71.9 | 3 | 2 | [[Homoharringtonine (drug)]] 5 µM 4.26× (z +19.2) | [[Panobinostat (drug)]] 5 µM 0.197× (z -15.3) |
| [[LS 180 (line)]] | wt | 134 | 2 | 3 | [[Homoharringtonine (drug)]] 5 µM 3.19× (z +14.1) | [[Panobinostat (drug)]] 5 µM 0.172× (z -15.2) |
| [[AsPC-1 (line)]] | alt | 73.7 | 1 | 3 | [[Homoharringtonine (drug)]] 5 µM 4.07× (z +18.0) | [[Panobinostat (drug)]] 5 µM 0.173× (z -16.0) |
| [[HOP62 (line)]] | alt | 47.9 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.48× (z +15.4) | — |
| [[HT-29 (line)]] | alt | 74.1 | 1 | 3 | [[Homoharringtonine (drug)]] 5 µM 3.57× (z +15.3) | [[Panobinostat (drug)]] 5 µM 0.182× (z -14.4) |
| [[J82 (line)]] | alt | 89.5 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.92× (z +21.4) | — |
| [[SK-MEL-2 (line)]] | alt | 176 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.152× (z -15.3) |
| [[SNU-1 (line)]] | wt | 97.1 | 4 | 0 | [[Harringtonine (drug)]] 0.5 µM 3.94× (z +11.0) | — |
| [[KATO III (line)]] | alt | 32.6 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +11.5) | [[Panobinostat (drug)]] 5 µM 0.305× (z -9.1) |
| [[NCI-H23 (line)]] | alt | 29.2 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.99× (z +10.9) | [[Dinaciclib (drug)]] 0.05 µM 0.254× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[PANC-1 (line)]] | alt | 33.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.21× (z +23.6) | — |
| [[AN3 CA (line)]] | alt | 76.2 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.82× (z +11.6) | [[Panobinostat (drug)]] 0.5 µM 0.120× (z -11.2) |
| [[COLO 205 (line)]] | alt | 28.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.52× (z +14.4) | — |
| [[NCI-H2030 (line)]] | alt | 69.6 | 2 | 0 | [[Harringtonine (drug)]] 5 µM 3.45× (z +10.8) | — |
| [[SHP-77 (line)]] | alt | 42.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.31× (z +12.5) | — |
| [[A-427 (line)]] | wt | 60.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.143× (z -17.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[H4 (line)]] | wt | 92.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.08× (z +11.8) | — |
| [[NCI-H661 (line)]] | alt | 37.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0498× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[RKO (line)]] | wt | 34.0 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.41× (z +10.6) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SW 1271 (line)]] | alt | 96.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.93× (z +8.9) | — |
| [[C-33 A (line)]] | alt | 8.91 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 49.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 54.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 52.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 15.8 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 148 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 59.7 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 17.0 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6014), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC00882]] | +0.68 | +0.60 / +0.49 | both halves | 1e-05 |  |
| [[CAMK2D]] | +0.68 | +0.68 / +0.52 | both halves | 1e-05 |  |
| [[PATL2]] | +0.64 | +0.54 / +0.45 | both halves | 3e-05 |  |
| [[ZBTB1]] | +0.63 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[DRAM1]] | +0.63 | +0.62 / +0.43 | both halves | 3e-05 |  |
| [[FOSL2]] | +0.62 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[MAP3K2-DT]] | +0.62 | +0.61 / +0.35 | both halves | 1e-04 |  |
| [[WAC-AS1]] | +0.61 | +0.56 / +0.34 | both halves | 1e-04 |  |
| [[TAPBPL]] | +0.61 | +0.53 / +0.47 | both halves | 2e-05 |  |
| [[STAT5A]] | +0.61 | +0.57 / +0.42 | both halves | 4e-05 |  |
| [[RIPK2-DT]] | +0.61 | +0.55 / +0.44 | both halves | 3e-05 |  |
| [[TFAP2A]] | +0.60 | +0.62 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[INTS4]] | -0.63 | -0.56 / -0.59 | both halves | 1e-05 |  |
| [[STARD3]] | -0.58 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[ERI3]] | -0.58 | -0.54 / -0.40 | both halves | 5e-05 |  |
| [[WRN]] | -0.58 | -0.52 / -0.42 | both halves | 4e-05 |  |
| [[ZCCHC17]] | -0.56 | -0.54 / -0.41 | both halves | 4e-05 |  |
| [[FXYD5]] | -0.56 | -0.54 / -0.41 | both halves | 4e-05 |  |
| [[STRAP]] | -0.56 | -0.46 / -0.37 | both halves | 9e-05 |  |
| [[RNF216]] | -0.56 | -0.58 / -0.38 | both halves | 7e-05 |  |
| [[NAPG]] | -0.56 | -0.55 / -0.25 | both halves | 4e-04 |  |
| [[IQCB1]] | -0.56 | -0.59 / -0.44 | both halves | 3e-05 |  |
| [[DCAF13]] | -0.55 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[PPM1F]] | -0.55 | -0.50 / -0.39 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MSC]] | B | MSC activity raises CPEB2's level | lines that do not express MSC (34) vs lines expressing it (16) | 2.26× lower at baseline in the lines without MSC | 0.036 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ITGA4, MMP2, SPARC |
| [[ZNF215]] | B | ZNF215 activity raises CPEB2's level | lines that do not express ZNF215 (12) vs lines expressing it (38) | 1.86× lower at baseline in the lines without ZNF215 | 0.060 | ⚠ within organs, on part of the lines; also absent: ENSG00000283415, ENSG00000291143 |
| [[THBD]] | B | THBD activity raises CPEB2's level | lines that do not express THBD (28) vs lines expressing it (22) | 1.61× lower at baseline in the lines without THBD | 0.061 | ⚠ within organs, on part of the lines; also absent: EFEMP1, KRT7, LINC02742 |
| [[GATA6]] | B | GATA6 activity raises CPEB2's level | lines that do not express GATA6 (18) vs lines expressing it (32) | 1.84× lower at baseline in the lines without GATA6 | 0.093 | ⚠ within organs, on part of the lines; also absent: ENSG00000264825, CDA, SPTLC3 |
| [[GULP1]] | C | GULP1 activity raises CPEB2's level | lines that do not express GULP1 (4) vs lines expressing it (46) | 2.83× lower at baseline in the lines without GULP1 | 0.080 | ⚠ few lines (4 vs 46); across organs; also absent: RND3, SFXN3, LRRCC1 |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GUCY2C-AS1]] | C | CPEB2 activity lowers GUCY2C-AS1's level | lines that do not express CPEB2 (3) vs lines expressing it (47) | 2.89× higher at baseline in the lines without CPEB2 | 0.020 | ⚠ few lines (3 vs 47); across organs; also absent: SFXN3, CDKN1A, LRIG3; maybe low, not absent |
| [[CAMK2D]] | C | CPEB2 activity raises CAMK2D's level | lines that do not express CPEB2 (3) vs lines expressing it (47) | 3.06× lower at baseline in the lines without CPEB2 | 0.046 | ⚠ few lines (3 vs 47); across organs; also absent: SFXN3, CDKN1A, LRIG3; maybe low, not absent; co-absent with the target |
| [[SLC12A7]] | C | CPEB2 activity strengthens SLC12A7's drug response | lines that do not express CPEB2 (3) vs lines expressing it (39) | the lines without CPEB2 respond 0.51× as strongly (z diff +2.24); strongest at Homoharringtonine 0.5 µM: 0.84x vs 3.47x (z diff +7.3) | 0.081 | ⚠ few lines (3 vs 47); across organs; also absent: SFXN3, CDKN1A, LRIG3; maybe low, not absent; target measured in part of the lines; artifact flags |

## Where it sits

- **Module**: [[Module 068]]; 73 genes; this gene is in the **+** arm (projection on the module's main direction 0.706). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (19.7, 13.1); signed map (46.9, 13.6). **Vector** length 108, 32.3% of its response variance represented; |z| ≥ 3 in 1,293 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +9.6 | +18.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | +9.0 | +17.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +7.8 | +28.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +7.7 | +7.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.6 | +3.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.8 | +2.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +4.3 | +2.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.1 | +3.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +3.7 | +2.0 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | -5.7 | -3.8 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -5.4 | -2.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -5.3 | -15.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | -4.9 | -18.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.3 | -2.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.6 | -4.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.5 | -0.5 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | -1.9 | -1.5 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.7 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | cytoplasmic polyadenylation element binding protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p15.32 — chr4:15,002,481-15,070,153 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | RNA binding motif containing |
| Hallmark sets | CHOLESTEROL_HOMEOSTASIS |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7Z5Q1](https://www.uniprot.org/uniprotkb/Q7Z5Q1) (Cytoplasmic polyadenylation element-binding protein 2):

> May play a role in translational regulation of stored mRNAs in transcriptionally inactive haploid spermatids. Binds to poly(U) RNA oligomers (By similarity). Required for cell cycle progression, specifically for the transition from metaphase to anaphase.

**Summary**, from NCBI Gene [132864](https://www.ncbi.nlm.nih.gov/gene/132864):

> The protein encoded by this gene is highly similar to cytoplasmic polyadenylation element binding protein (CPEB), an mRNA-binding protein that regulates cytoplasmic polyadenylation of mRNA as a trans factor in oogenesis and spermatogenesis. Studies of the similar gene in mice suggested a possible role of this protein in transcriptionally inactive haploid spermatids. Alternatively spliced transcript variants encoding distinct isoforms have been described. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:21745](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21745) · Entrez [132864](https://www.ncbi.nlm.nih.gov/gene/132864) · UniProt [Q7Z5Q1](https://www.uniprot.org/uniprotkb/Q7Z5Q1) · Ensembl [ENSG00000137449](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137449)

## Data

Gene col 6014: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6014); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6014, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6014]; `tensor/DDL_lfc|DDL_z.npy` [6014]; `embed/gene_vectors.npy` [6014]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6014 or target_col == 6014). Every well: [[CPEB2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CPEB2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
