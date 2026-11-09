---
symbol: "APOO"
type: "gene"
col: 11579
ensembl_id: "ENSG00000184831"
name: "apolipoprotein O"
location: "Xp22.11"
module: 25
arm: "+"
pooled_cpm: 20.35
n_lines_expressing: 49
n_dd_up: 15
n_dd_down: 5
n_dd_up_clean: 5
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# APOO

*apolipoprotein O* — Xp22.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (10 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.10× (z +15.8, q 0e+00, up in 38 of 47 measured lines) ⚠ cell-cycle shift, explains ~33% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.05 µM: 1.41× (z +7.3, q 2e-11, up in 23 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.695× (z -7.7, q 7e-12, down in 21 of 47 measured lines).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMTC3]] (+0.58, fdr 1e-04), [[SSX2IP]] (+0.57, fdr 3e-05), [[DLD]] (+0.57, fdr 1e-05); moves opposite to [[RBBP6]] (-0.55, fdr 4e-04), [[CASS4]] (-0.53, fdr 8e-05), [[ATXN1L]] (-0.52, fdr 8e-05).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 13 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11579.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **2.10×** | +15.8 | 0e+00 | 38/47 (Hs 766T, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **2.00×** | +14.8 | 0e+00 | 38/47 (Hs 766T, CFPAC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **1.96×** | +13.7 | 1e-40 | 23/29 (MIA PaCa-2, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **1.85×** | +13.0 | 1e-36 | 29/40 (A549, NCI-H2030, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.84×** | +12.9 | 4e-36 | 35/47 (Hs 766T, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **1.51×** | +8.1 | 6e-14 | 24/35 (NCI-H1573, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.41×** | +7.3 | 2e-11 | 23/47 (CFPAC-1, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.35×** | +6.4 | 1e-08 | 18/46 (CFPAC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.23×** | +6.4 | 1e-08 | 19/47 (CFPAC-1, SNU-423, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~58% of this change | **1.29×** | +5.2 | 1e-05 | 16/42 (COLO 205, A498, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.26×** | +5.0 | 4e-05 | 17/45 (C32, SNU-423, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.24×** | +4.6 | 2e-04 | 13/46 (HOP62, HEC-1-A, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.22×** | +4.3 | 7e-04 | 12/47 (C32, HOP62, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **1.22×** | +4.2 | 1e-03 | 12/46 (A549, SNU-423, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.42×** | +3.9 | 0.004 | 7/47 (CFPAC-1, KATO III, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Berbamine (drug)]] 0.05 µM |  | 1.16× | +3.2 | 0.048 | 5/47 (A-172, KATO III, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11579.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.695×** | -7.7 | 7e-12 | 21/47 (PANC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.774×** | -5.4 | 2e-05 | 20/45 (A-172, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.793×** | -4.6 | 7e-04 | 11/47 (SW480, HS-578T, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.823×** | -4.1 | 0.005 | 17/45 (MIA PaCa-2, C-33 A, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.833×** | -3.9 | 0.013 | 20/45 (NCI-H460, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 0.835× | -3.8 | 0.013 | 16/45 (A-172, LS 180, …) | two highest doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.845× | -3.6 | 0.031 | 10/46 (BT-474, HS-578T, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | 0.857× | -3.3 | 0.073 | 10/45 (A-172, RPMI-7951, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.858× | -3.2 | 0.073 | 5/46 (A-172, LOX-IMVI, …) | top dose only |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | 0.862× | -3.1 | 0.088 | 4/45 (COLO 205, A-172, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 5 µM |  | 0.857× | -3.1 | 0.088 | 9/45 (A-172, SHP-77, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.41 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11579. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 8.92 | 3 (2 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 3.22× (z +9.0) | — |
| [[Hs 766T (line)]] | wt | 17.7 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.37× (z +10.1) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[A498 (line)]] | wt | 14.5 | 0 | 1 | — | [[GSK1059615 (drug)]] 0.5 µM 0.184× (z -9.5) |
| [[HepG2_C3A (line)]] | wt | 12.1 | 0 | 1 | — | [[Rifaximin (drug)]] 0.05 µM 0.0615× (z -10.1) |
| [[NCI-H460 (line)]] | wt | 25.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.337× (z -10.6) ⚠ toxic; transcription drop |
| [[NCI-H661 (line)]] | alt | 35.0 | 0 | 1 | — | [[Berberine (chloride hydrate) (drug)]] 0.05 µM 0.0665× (z -8.8) |
| [[PANC-1 (line)]] | alt | 22.6 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.433× (z -8.6) |
| [[SHP-77 (line)]] | alt | 24.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.135× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[SK-MEL-2 (line)]] | alt | 29.0 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.285× (z -8.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-1 (line)]] | wt | 12.6 | 0 | 1 | — | [[Isocorydine (drug)]] 0.5 µM 0.0826× (z -9.6) |
| [[SNU-423 (line)]] | alt | 23.0 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.01× (z +8.7) ⚠ cell-cycle shift, explains ~33% of this change | — |
| [[SW 900 (line)]] | alt | 11.3 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.138× (z -9.5) ⚠ transcription drop; cell-cycle shift, explains ~14% of this change |
| [[SW480 (line)]] | alt | 40.8 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.544× (z -11.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 49.0 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 33.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.79 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 35.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 22.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.93 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.22 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.59 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.16 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 37.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.74 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.33 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.64 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 30.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11579), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*50 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMTC3]] | +0.58 | +0.34 / +0.59 | both halves | 1e-04 |  |
| [[SSX2IP]] | +0.57 | +0.44 / +0.55 | both halves | 3e-05 |  |
| [[DLD]] | +0.57 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[USP14]] | +0.56 | +0.58 / +0.43 | both halves | 3e-05 |  |
| [[NDRG3]] | +0.55 | +0.36 / +0.50 | both halves | 9e-05 |  |
| [[STARD3NL]] | +0.53 | +0.38 / +0.43 | both halves | 6e-05 |  |
| [[HNRNPR]] | +0.51 | +0.54 / +0.43 | both halves | 3e-05 |  |
| [[ZDHHC21]] | +0.51 | +0.40 / +0.51 | both halves | 5e-05 |  |
| [[FAM98B]] | +0.50 | +0.48 / +0.49 | both halves | 2e-05 |  |
| [[MRPL42]] | +0.50 | +0.36 / +0.55 | both halves | 1e-04 |  |
| [[AGPS]] | +0.50 | +0.45 / +0.43 | both halves | 3e-05 |  |
| [[DHX9]] | +0.50 | +0.49 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*50 of its nearest partners move opposite, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBBP6]] | -0.55 | -0.25 / -0.55 | both halves | 4e-04 |  |
| [[CASS4]] | -0.53 | -0.37 / -0.40 | both halves | 8e-05 |  |
| [[ATXN1L]] | -0.52 | -0.37 / -0.45 | both halves | 8e-05 |  |
| [[CFAP53]] | -0.52 | -0.30 / -0.42 | both halves | 2e-04 |  |
| [[NUFIP2]] | -0.52 | -0.40 / -0.37 | both halves | 8e-05 |  |
| [[TOB2]] | -0.52 | -0.49 / -0.44 | both halves | 3e-05 |  |
| [[DARS1-AS1]] | -0.52 | -0.35 / -0.45 | both halves | 1e-04 |  |
| [[CCDC59]] | -0.52 | -0.21 / -0.55 | both halves | 7e-04 |  |
| [[ANKRD17-DT]] | -0.51 | -0.24 / -0.48 | both halves | 5e-04 |  |
| [[RSBN1]] | -0.51 | -0.33 / -0.50 | both halves | 1e-04 |  |
| [[FAM117A]] | -0.51 | -0.39 / -0.33 | both halves | 1e-04 |  |
| [[ANKHD1-EIF4EBP3]] | -0.50 | -0.24 / -0.45 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers APOO's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers APOO's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.372). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-24.4, -15.3); signed map (-17.3, -43.7). **Vector** length 72.1, 11.8% of its response variance represented; |z| ≥ 3 in 944 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | +6.3 | +13.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | +5.8 | +13.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | +4.5 | +8.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.3 | +6.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.5 | +4.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.7 | +2.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.6 | +2.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.4 | +3.9 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.6 | -0.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.6 | -7.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.4 | -4.1 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.2 | -3.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.1 | -2.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.9 | -3.2 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -1.6 | -1.6 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -1.5 | -2.1 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.5 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | apolipoprotein O |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp22.11 — chrX:23,833,353-23,907,938 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC4825, My025, Mic23, MIC26, MICOS26; previously FAM121B |
| Gene groups (HGNC) | Apolipoproteins; Mitochondrial contact site and cristae organizing system subunits |
| Reactome | 3 pathways, smallest: Cristae formation; Mitochondrial biogenesis; Organelle biogenesis and maintenance |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BUR5](https://www.uniprot.org/uniprotkb/Q9BUR5) (MICOS complex subunit MIC26):

> Component of the MICOS complex, a large protein complex of the mitochondrial inner membrane that plays crucial roles in the maintenance of crista junctions, inner membrane architecture, and formation of contact sites to the outer membrane. Plays a crucial role in crista junction formation and mitochondrial function. Can promote cardiac lipotoxicity by enhancing mitochondrial respiration and fatty acid metabolism in cardiac myoblasts. Promotes cholesterol efflux from macrophage cells. Detected …

**Summary**, from NCBI Gene [79135](https://www.ncbi.nlm.nih.gov/gene/79135):

> This gene is a member of the apolipoprotein family. Members of this protein family are involved in the transport and metabolism of lipids. The encoded protein associates with HDL, LDL and VLDL lipoproteins and is characterized by chondroitin-sulfate glycosylation. This protein may be involved in preventing lipid accumulation in the myocardium in obese and diabetic patients. Alternative splicing results in multiple transcript variants. Pseudogenes of this gene are found on chromosomes 3, 4, 5, …

**Accessions** — [HGNC:28727](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28727) · Entrez [79135](https://www.ncbi.nlm.nih.gov/gene/79135) · UniProt [Q9BUR5](https://www.uniprot.org/uniprotkb/Q9BUR5) · Ensembl [ENSG00000184831](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000184831)

## Data

Gene col 11579: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11579); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11579, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11579]; `tensor/DDL_lfc|DDL_z.npy` [11579]; `embed/gene_vectors.npy` [11579]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11579 or target_col == 11579). Every well: [[APOO — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/APOO.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
