---
symbol: "VCP"
type: "gene"
col: 9100
ensembl_id: "ENSG00000165280"
name: "valosin containing protein"
location: "9p13.3"
module: 60
arm: "+"
pooled_cpm: 123.17
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 4
n_dd_up_clean: 5
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/060"]
generated_by: "tahoemap"
---

# VCP

*valosin containing protein* — 9p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (9 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 0.5 µM: 3.29× (z +23.2, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 0.5 µM: 0.753× (z -5.6, q 1e-05, down in 32 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PSMD1]] (+0.74, fdr 7e-06), [[HSP90AA2P]] (+0.71, fdr 7e-06), [[SFXN5]] (+0.70, fdr 7e-06); moves opposite to [[VPS26C]] (-0.58, fdr 1e-05), [[RCHY1]] (-0.57, fdr 1e-05), [[PER1]] (-0.57, fdr 2e-05).
> It sits in the **+** arm of [[Module 060]] (heat shock).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 11 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9100.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **3.29×** | +23.2 | 0e+00 | 48/48 (SW480, HT-29, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **3.20×** | +22.7 | 0e+00 | 48/48 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.79×** | +18.9 | 0e+00 | 48/48 (SW480, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.24×** | +15.7 | 0e+00 | 46/48 (HT-29, AsPC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **1.68×** | +10.0 | 1e-21 | 41/49 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **1.63×** | +9.2 | 4e-18 | 37/44 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.92×** | +9.1 | 9e-18 | 45/49 (LOX-IMVI, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.31×** | +8.5 | 1e-15 | 42/45 (SW480, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **1.30×** | +7.1 | 9e-11 | 27/48 (A498, NCI-H1573, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **1.44×** | +6.5 | 4e-09 | 33/45 (PANC-1, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~38% of this change | **1.27×** | +4.4 | 6e-04 | 28/47 (PANC-1, NCI-H23, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.23×** | +4.0 | 0.003 | 26/48 (NCI-H1792, AsPC-1, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 5 µM |  | 1.15× | +3.7 | 0.009 | 10/48 (HOP62, MIA PaCa-2, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.21×** | +3.7 | 0.009 | 23/48 (A498, NCI-H1573, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.20×** | +3.6 | 0.013 | 23/47 (HOP62, HT-29, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 1.17× | +3.0 | 0.073 | 15/47 (HT-29, NCI-H23, …) | two highest doses |  |
| [[Vilanterol (drug)]] 5 µM |  | 1.12× | +3.0 | 0.076 | 3/49 (SHP-77, Hs 766T, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9100.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.753×** | -5.6 | 1e-05 | 32/49 (SW480, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **0.818×** | -5.5 | 1e-05 | 24/48 (NCI-H2347, LoVo, …) | all doses, stronger at high dose | position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **0.784×** | -4.8 | 3e-04 | 33/48 (KATO III, LoVo, …) | rises with dose |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.815×** | -3.9 | 0.016 | 27/49 (HepG2/C3A, BT-474, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.836× | -3.5 | 0.040 | 22/48 (KATO III, AsPC-1, …) | rises with dose |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 0.836× | -3.5 | 0.040 | 19/48 (KATO III, LoVo, …) | rises with dose |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | 0.885× | -3.4 | 0.055 | 3/48 (SHP-77, NCI-H661, …) | top dose only |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | 0.843× | -3.4 | 0.055 | 19/48 (H4, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 0.888× | -3.3 | 0.063 | 13/48 (KATO III, A-427, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.856× | -3.1 | 0.13 | 13/48 (NCI-H23, HT-29, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9100. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 199 | 7 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +13.5) ⚠ cell-cycle shift, explains ~64% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 2.23× (z +12.7) | — |
| [[BT-474 (line)]] | alt | 581 | 4 | 3 (3 ⚠) | [[Auranofin (drug)]] 5 µM 2.75× (z +14.9) | [[Homoharringtonine (drug)]] 0.5 µM 0.482× (z -10.8) ⚠ cell-cycle shift, explains ~35% of this change |
| [[LOX-IMVI (line)]] | wt | 85.7 | 7 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 6.10× (z +19.0) | — |
| [[PANC-1 (line)]] | alt | 142 | 7 (3 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.64× (z +17.6) | — |
| [[A-172 (line)]] | wt | 131 | 5 (1 ⚠) | 1 | [[Ixazomib citrate (drug)]] 0.5 µM 3.02× (z +13.6) | [[Homoharringtonine (drug)]] 0.05 µM 0.429× (z -10.6) |
| [[MIA PaCa-2 (line)]] | alt | 87.9 | 6 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.71× (z +14.3) | — |
| [[NCI-H1792 (line)]] | alt | 67.7 | 6 (3 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.91× (z +13.5) | — |
| [[AsPC-1 (line)]] | alt | 125 | 4 | 1 | [[Ixazomib citrate (drug)]] 0.5 µM 3.72× (z +15.8) | [[Radotinib (drug)]] 5 µM 0.583× (z -9.0) |
| [[SNU-423 (line)]] | alt | 87.8 | 5 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.19× (z +16.0) | — |
| [[SW480 (line)]] | alt | 119 | 5 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.22× (z +21.7) | — |
| [[A549 (line)]] | wt | 124 | 4 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.10× (z +15.1) | — |
| [[CFPAC-1 (line)]] | alt | 53.9 | 4 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.77× (z +16.7) | — |
| [[COLO 205 (line)]] | alt | 95.7 | 4 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 6.21× (z +14.1) | — |
| [[H4 (line)]] | wt | 182 | 4 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.51× (z +15.0) | — |
| [[HEC-1-A (line)]] | alt | 77.1 | 4 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.48× (z +17.8) | — |
| [[HOP62 (line)]] | alt | 123 | 4 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.32× (z +18.5) | — |
| [[Hs 766T (line)]] | wt | 108 | 4 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.50× (z +12.9) | — |
| [[HS-578T (line)]] | alt | 108 | 4 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.02× (z +12.9) | — |
| [[HT-29 (line)]] | alt | 142 | 4 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.49× (z +19.5) | — |
| [[KATO III (line)]] | alt | 203 | 4 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.16× (z +16.8) | — |
| [[LoVo (line)]] | wt | 139 | 4 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.83× (z +18.1) | — |
| [[NCI-H1573 (line)]] | alt | 87.6 | 4 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.67× (z +17.1) | — |
| [[NCI-H460 (line)]] | wt | 83.1 | 4 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.89× (z +16.5) | — |
| [[Panc 03.27 (line)]] | alt | 108 | 4 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.73× (z +15.5) | — |
| [[SK-MEL-2 (line)]] | alt | 96.4 | 4 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.26× (z +12.3) | — |
| [[SW 900 (line)]] | alt | 103 | 4 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.04× (z +11.7) | — |
| [[SW1417 (line)]] | alt | 109 | 4 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.90× (z +13.3) | — |
| [[A-427 (line)]] | wt | 106 | 3 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.64× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 2.61× (z +10.6) | — |
| [[C32 (line)]] | wt | 51.9 | 3 | 0 | [[Auranofin (drug)]] 5 µM 6.06× (z +15.2) | — |
| [[HCT15 (line)]] | alt | 135 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.72× (z +15.6) | — |
| [[HepG2_C3A (line)]] | wt | 124 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.51× (z +12.4) | — |
| [[hTERT-HPNE (line)]] | wt | 131 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.17× (z +14.8) | — |
| [[J82 (line)]] | alt | 147 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.20× (z +10.2) | — |
| [[LS 180 (line)]] | wt | 104 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.09× (z +15.7) | — |
| [[NCI-H2347 (line)]] | alt | 74.5 | 3 | 0 | [[Bortezomib (drug)]] 0.05 µM 3.19× (z +13.9) | — |
| [[RKO (line)]] | wt | 123 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.38× (z +10.4) | — |
| [[RPMI-7951 (line)]] | alt | 96.7 | 3 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.31× (z +11.3) | — |
| [[C-33 A (line)]] | alt | 138 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.08× (z +11.3) | — |
| [[NCI-H2030 (line)]] | alt | 98.4 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.71× (z +12.3) | — |
| [[SW48 (line)]] | wt | 108 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.81× (z +12.2) | — |
| [[NCI-H23 (line)]] | alt | 268 | 1 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.30× (z +10.5) | — |
| [[SHP-77 (line)]] | alt | 70.3 | 1 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.48× (z +8.7) | — |
| [[SNU-1 (line)]] | wt | 77.7 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.31× (z +9.1) | — |
| [[AN3 CA (line)]] | alt | 120 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 105 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 91.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 98.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 160 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 91.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9100), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSMD1]] | +0.74 | +0.71 / +0.75 | both halves | 7e-06 | pathway: ABC transporter disorders; STRING 778 |
| [[HSP90AA2P]] | +0.71 | +0.71 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[SFXN5]] | +0.70 | +0.67 / +0.69 | both halves | 7e-06 |  |
| [[HSP90AA1]] | +0.69 | +0.66 / +0.68 | both halves | 7e-06 | pathway: Aggrephagy; STRING 933 |
| [[PSMD12]] | +0.68 | +0.65 / +0.68 | both halves | 7e-06 | pathway: ABC transporter disorders; STRING 807 |
| [[PSMC4]] | +0.68 | +0.65 / +0.70 | both halves | 7e-06 | same gene group; pathway: ABC transporter disorders; STRING 855 |
| [[STIP1]] | +0.66 | +0.66 / +0.65 | both halves | 7e-06 | STRING 684 |
| [[PSMD11]] | +0.66 | +0.70 / +0.65 | both halves | 7e-06 | pathway: ABC transporter disorders; STRING 785 |
| [[UTP11]] | +0.65 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[CCT6A]] | +0.64 | +0.61 / +0.68 | both halves | 7e-06 | STRING 545 |
| [[SERPINH1]] | +0.64 | +0.68 / +0.63 | both halves | 7e-06 | pathway: Cellular response to heat stress |
| [[PSMC3]] | +0.63 | +0.69 / +0.57 | both halves | 9e-06 | same gene group; pathway: ABC transporter disorders; STRING 790 |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VPS26C]] | -0.58 | -0.58 / -0.54 | both halves | 1e-05 |  |
| [[RCHY1]] | -0.57 | -0.51 / -0.62 | both halves | 1e-05 | pathway: DNA Damage Bypass |
| [[PER1]] | -0.57 | -0.48 / -0.60 | both halves | 2e-05 |  |
| [[ZNF330]] | -0.56 | -0.42 / -0.66 | both halves | 4e-05 |  |
| [[ARHGAP12]] | -0.56 | -0.59 / -0.53 | both halves | 1e-05 |  |
| [[RCOR3]] | -0.56 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[ZNF670]] | -0.56 | -0.52 / -0.57 | both halves | 1e-05 |  |
| [[YY1AP1]] | -0.55 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[NR1D1]] | -0.55 | -0.41 / -0.61 | both halves | 4e-05 |  |
| [[SNAPC1]] | -0.53 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[ABCA5]] | -0.53 | -0.48 / -0.53 | both halves | 2e-05 | pathway: ABC-family protein mediated transport |
| [[MRPL39]] | -0.53 | -0.48 / -0.52 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 060]] — heat shock; 78 genes; this gene is in the **+** arm (projection on the module's main direction 0.724). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-21.1, -11.8); signed map (-27.3, -28.6). **Vector** length 128, 42.2% of its response variance represented; |z| ≥ 3 in 1,169 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Attenuation phase* (reactome, mean cos +0.51 to 13); *HSP90 chaperone cycle for steroid hormone receptors (SHR) in the presence of ligand* (reactome, mean cos +0.53 to 12); *mTORC1 signaling* (hallmark, mean cos +0.53 to 13).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +12.4 | +18.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +12.2 | +22.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +10.9 | +23.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +9.2 | +15.7 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +7.4 | +8.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +5.6 | +9.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.6 | +2.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.6 | +0.8 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -6.2 | -1.2 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.8 | +1.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -5.6 | -5.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.3 | -5.5 |
|  | [[Radotinib (drug)]] 5 µM |  | -4.4 | -2.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.2 | -2.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | -4.1 | -4.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | -4.0 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | valosin containing protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p13.3 — chr9:35,053,928-35,072,668 (-) |
| Ensembl biotype | protein_coding |
| Also known as | IBMPFD, p97, CDC48, TERA |
| Gene groups (HGNC) | AAA ATPases; VCP-Ufd1-Npl4 complex subunits |
| Reactome | 57 pathways, smallest: Attachment and Entry_9678110; Josephin domain DUBs; Protein methylation |
| Matched by | ensembl_id |

**Function**, from UniProt [P55072](https://www.uniprot.org/uniprotkb/P55072) (Transitional endoplasmic reticulum ATPase):

> Necessary for the fragmentation of Golgi stacks during mitosis and for their reassembly after mitosis. Involved in the formation of the transitional endoplasmic reticulum (tER). The transfer of membranes from the endoplasmic reticulum to the Golgi apparatus occurs via 50-70 nm transition vesicles which derive from part-rough, part-smooth transitional elements of the endoplasmic reticulum (tER). Vesicle budding from the tER is an ATP-dependent process. The ternary complex containing UFD1, VCP …

**Summary**, from NCBI Gene [7415](https://www.ncbi.nlm.nih.gov/gene/7415):

> This gene encodes a member of the AAA ATPase family of proteins. The encoded protein plays a role in protein degradation, intracellular membrane fusion, DNA repair and replication, regulation of the cell cycle, and activation of the NF-kappa B pathway. This protein forms a homohexameric complex that interacts with a variety of cofactors and extracts ubiquitinated proteins from lipid membranes or protein complexes. Mutations in this gene cause IBMPFD (inclusion body myopathy with paget disease …

**Accessions** — [HGNC:12666](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12666) · Entrez [7415](https://www.ncbi.nlm.nih.gov/gene/7415) · UniProt [P55072](https://www.uniprot.org/uniprotkb/P55072) · Ensembl [ENSG00000165280](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165280)

## Data

Gene col 9100: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9100); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9100, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9100]; `tensor/DDL_lfc|DDL_z.npy` [9100]; `embed/gene_vectors.npy` [9100]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9100 or target_col == 9100). Every well: [[VCP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/VCP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
