---
symbol: "PRKCH"
type: "gene"
col: 377
ensembl_id: "ENSG00000027075"
name: "protein kinase C eta"
location: "14q23.1"
module: 61
arm: "+"
pooled_cpm: 35.14
n_lines_expressing: 44
n_dd_up: 8
n_dd_down: 10
n_dd_up_clean: 7
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 3
direction_downstream: 3
tags: ["gene", "module/061"]
generated_by: "tahoemap"
---

# PRKCH

*protein kinase C eta* — 14q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 1.86× (z +11.9, q 7e-30, up in 30 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.650× (z -8.3, q 8e-14, down in 24 of 39 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change. The strongest without an alert is [[Belumosudil (drug)]] 5 µM: 0.812× (z -3.8, q 0.010, down in 14 of 41 measured lines).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARHGEF26-AS1]] (+0.54, fdr 4e-05), [[TLE2]] (+0.52, fdr 6e-05), [[LINC02006]] (+0.52, fdr 4e-05); moves opposite to [[ENTPD5]] (-0.47, fdr 4e-04), [[DNAJC16]] (-0.40, fdr 0.002, ⚠ not reproduced), [[TMEM250]] (-0.39, fdr 2e-04), [[POLI]] (-0.39, fdr 1e-04).
> It is in [[Module 061]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[PRKCH-AS1]] → it (grade B ⚠); 3 go from it, the strongest it → [[C1orf54]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 377.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.86×** | +11.9 | 7e-30 | 30/41 (HOP62, HEC-1-A, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.50×** | +11.0 | 9e-26 | 22/42 (CFPAC-1, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.46×** | +10.3 | 1e-22 | 23/42 (NCI-H2030, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.61×** | +9.2 | 7e-18 | 28/43 (C32, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.72×** | +5.4 | 6e-06 | 17/42 (HOP62, A-427, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.30×** | +5.0 | 6e-05 | 16/42 (NCI-H2030, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.28×** | +4.4 | 7e-04 | 14/42 (NCI-H460, SHP-77, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.21×** | +3.6 | 0.021 | 8/42 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | 1.18× | +3.2 | 0.086 | 11/41 (NCI-H1792, A549, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.12× | +3.2 | 0.088 | 13/42 (MIA PaCa-2, SNU-423, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 8 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 377.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.650×** | -8.3 | 8e-14 | 24/39 (Hs 766T, SNU-1, …) | all doses, flat | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.653×** | -7.9 | 1e-12 | 25/40 (HS-578T, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.775×** | -4.9 | 2e-04 | 20/42 (LoVo, Hs 766T, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **0.770×** | -4.8 | 2e-04 | 18/32 (Panc 03.27, Hs 766T, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.766×** | -4.7 | 3e-04 | 21/35 (SNU-1, A-427, …) | all doses, flat | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.814×** | -4.0 | 0.007 | 12/42 (SW1417, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.812×** | -3.8 | 0.010 | 14/41 (SNU-423, hTERT-HPNE, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.827×** | -3.6 | 0.019 | 14/43 (MIA PaCa-2, NCI-H2347, …) | inconsistent across doses |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.697×** | -3.6 | 0.019 | 13/41 (H4, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | **0.832×** | -3.4 | 0.039 | 4/42 (MIA PaCa-2, AN3 CA, …) | top dose only |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | 0.844× | -3.2 | 0.059 | 10/41 (H4, A498, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.847× | -3.2 | 0.071 | 8/41 (SNU-1, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~88% of this change | 0.853× | -3.1 | 0.098 | 17/40 (Panc 03.27, HT-29, …) | inconsistent across doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.00 per unit of S-phase module lfc, -0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 377. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 174 | 0 | 8 (8 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.162× (z -16.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[HT-29 (line)]] | alt | 111 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.227× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[Panc 03.27 (line)]] | alt | 101 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.243× (z -14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[SNU-1 (line)]] | wt | 72.0 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.115× (z -14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.391× (z -8.7) |
| [[A-427 (line)]] | wt | 36.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.261× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[A498 (line)]] | wt | 21.1 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.97× (z +8.5) | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -15.0) ⚠ cell-cycle shift, would explain all of this change |
| [[C32 (line)]] | wt | 19.0 | 2 | 0 | [[Auranofin (drug)]] 5 µM 5.36× (z +10.8) | — |
| [[CFPAC-1 (line)]] | alt | 51.5 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.57× (z +13.2) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.402× (z -8.6) ⚠ toxic |
| [[HS-578T (line)]] | alt | 19.5 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.132× (z -10.8) ⚠ toxic |
| [[KATO III (line)]] | alt | 16.3 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.58× (z +10.2) | [[Digitoxin (drug)]] 5 µM 0.121× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[LS 180 (line)]] | wt | 42.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.249× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[NCI-H1792 (line)]] | alt | 21.2 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.32× (z +11.0) | [[Dinaciclib (drug)]] 0.5 µM 0.246× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[NCI-H2030 (line)]] | alt | 35.4 | 2 (1 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 2.29× (z +9.8) | — |
| [[NCI-H23 (line)]] | alt | 14.6 | 2 | 0 | [[Auranofin (drug)]] 5 µM 6.36× (z +8.9) | — |
| [[SHP-77 (line)]] | alt | 8.97 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.00× (z +10.2) | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.113× (z -8.7) |
| [[SW 900 (line)]] | alt | 22.6 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 5.70× (z +10.6) | [[Dinaciclib (drug)]] 5 µM 0.163× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[H4 (line)]] | wt | 25.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.241× (z -9.3) ⚠ cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 9.01 | 1 | 0 | [[Auranofin (drug)]] 5 µM 7.00× (z +11.2) | — |
| [[HOP62 (line)]] | alt | 14.7 | 1 | 0 | [[Auranofin (drug)]] 5 µM 7.61× (z +12.0) | — |
| [[LoVo (line)]] | wt | 60.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.364× (z -10.8) ⚠ cell-cycle shift, explains ~39% of this change |
| [[NCI-H1573 (line)]] | alt | 79.6 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.363× (z -10.0) ⚠ toxic |
| [[NCI-H460 (line)]] | wt | 18.2 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.18× (z +9.0) | — |
| [[RPMI-7951 (line)]] | alt | 17.3 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0929× (z -11.4) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 77.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.66 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 145 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 20.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 47.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 63.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.05 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 23.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.33 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 43.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 69.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 68.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 39.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.22 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 5.56 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 4.61 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 47.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 13.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 377), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 6 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARHGEF26-AS1]] | +0.54 | +0.41 / +0.53 | both halves | 4e-05 |  |
| [[TLE2]] | +0.52 | +0.38 / +0.55 | both halves | 6e-05 |  |
| [[LINC02006]] | +0.52 | +0.42 / +0.44 | both halves | 4e-05 |  |
| [[TMEFF2]] | +0.49 | +0.37 / +0.48 | both halves | 9e-05 |  |
| [[HRG-AS1]] | +0.49 | +0.40 / +0.38 | both halves | 7e-05 |  |
| [[CMAHP]] | +0.49 | +0.43 / +0.39 | both halves | 6e-05 |  |
| [[PLCL1]] | +0.48 | +0.38 / +0.52 | both halves | 7e-05 |  |
| [[LINC02580]] | +0.47 | +0.32 / +0.52 | both halves | 2e-04 |  |
| [[CRLF1]] | +0.46 | +0.38 / +0.45 | both halves | 6e-05 |  |
| [[MEIOC]] | +0.46 | +0.29 / +0.43 | both halves | 3e-04 |  |
| [[CHRNA7]] | +0.46 | +0.31 / +0.50 | both halves | 2e-04 |  |
| [[PLXNC1]] | +0.46 | +0.31 / +0.44 | both halves | 2e-04 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ENTPD5]] | -0.47 | -0.26 / -0.45 | both halves | 4e-04 |  |
| [[DNAJC16]] | -0.40 | -0.14 / -0.39 | ⚠ not reproduced | 0.002 |  |
| [[TMEM250]] | -0.39 | -0.30 / -0.47 | both halves | 2e-04 |  |
| [[POLI]] | -0.39 | -0.36 / -0.36 | both halves | 1e-04 |  |
| [[ZNF624]] | -0.39 | -0.24 / -0.41 | both halves | 4e-04 |  |
| [[ST3GAL3]] | -0.39 | -0.45 / -0.32 | both halves | 2e-04 |  |
| [[MSS51]] | -0.39 | -0.29 / -0.38 | both halves | 2e-04 |  |
| [[PPP3CB]] | -0.39 | -0.29 / -0.39 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PRKCH-AS1]] | B | PRKCH-AS1 activity raises PRKCH's level | lines that do not express PRKCH-AS1 (34) vs lines expressing it (16) | 3.14× lower at baseline in the lines without PRKCH-AS1 | 0.001 | ⚠ within organs, on part of the lines; also absent: SLC5A1, TMEM30B, TMPRSS2; maybe low, not absent |
| [[LINC00457]] | B | LINC00457 activity raises PRKCH's level | lines that do not express LINC00457 (29) vs lines expressing it (21) | 1.82× lower at baseline in the lines without LINC00457 | 0.067 | ⚠ within organs, on part of the lines; also absent: LINC01440, LINC01456, NTS; maybe low, not absent |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers PRKCH's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C1orf54]] | B | PRKCH activity raises C1orf54's level | lines that do not express PRKCH (6) vs lines expressing it (44) | 1.54× lower at baseline in the lines without PRKCH | 0.054 | ⚠ within organs, on part of the lines; also absent: ENSG00000258989, ENSG00000284686, APBA1; maybe low, not absent |
| [[HOOK2]] | B | PRKCH activity raises HOOK2's level | lines that do not express PRKCH (6) vs lines expressing it (44) | 1.81× lower at baseline in the lines without PRKCH | 0.055 | ⚠ within organs, on part of the lines; also absent: ENSG00000258989, ENSG00000284686, APBA1; maybe low, not absent |
| cells under [[NVP-BHG712 (drug)]] 5 µM | B | PRKCH activity raises the cells' numbers under NVP-BHG712 5 µM (protects the cells) | lines that do not express PRKCH (6) vs lines expressing it (42) | the lines without PRKCH: 0.83× the cells of the other lines | 0.099 | ⚠ within organs, on part of the lines; also absent: ENSG00000258989, ENSG00000284686, APBA1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 061]] — Neuronal System; 78 genes; every member is in the + arm (projection on the module's main direction 0.375). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (13.3, 33.7); signed map (27.4, 21.5). **Vector** length 82.7, 15.8% of its response variance represented; |z| ≥ 3 in 970 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +9.5 | +11.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.5 | +10.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.1 | +9.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.9 | +11.0 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.8 | +2.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.1 | +2.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.1 | +1.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.1 | +0.6 |
| fall | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.2 | -3.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.6 | -3.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.4 | -2.4 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.3 | -1.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.2 | -4.0 |
|  | [[crizotinib (drug)]] 5 µM |  | -1.2 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | protein kinase C eta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q23.1 — chr14:61,187,559-61,550,976 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PKCη, PKC-L, PKCL; previously PRKCL |
| Gene groups (HGNC) | C2 domain containing protein kinases; Protein kinase C family |
| Hallmark sets | IL2_STAT5_SIGNALING |
| Reactome | 7 pathways, smallest: Effects of PIP2 hydrolysis; G alpha (z) signalling events; G alpha (q) signalling events |
| Matched by | ensembl_id |

**Function**, from UniProt [C0HM02](https://www.uniprot.org/uniprotkb/C0HM02) (PRKCH upstream open reading frame 2):

> Product of an upstream open reading frame (ORF) of PRKCH which regulates translation of the downstream protein kinase C eta (PKC-eta) ORF. Functions as a repressive element that maintains low basal levels of PKC-eta in growing cells but enhances its expression during stress conditions induced by amino acid starvation in a EIF2AK4/GCN2-dependent manner. In addition to its role in regulating PKC-eta translation, also inhibits the kinase activity of PKC-eta as well as other protein kinases …

**Summary**, from NCBI Gene [5583](https://www.ncbi.nlm.nih.gov/gene/5583):

> Protein kinase C (PKC) is a family of serine- and threonine-specific protein kinases that can be activated by calcium and the second messenger diacylglycerol. PKC family members phosphorylate a wide variety of protein targets and are known to be involved in diverse cellular signaling pathways. PKC family members also serve as major receptors for phorbol esters, a class of tumor promoters. Each member of the PKC family has a specific expression profile and is believed to play a distinct role in …

**Accessions** — [HGNC:9403](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9403) · Entrez [5583](https://www.ncbi.nlm.nih.gov/gene/5583) · UniProt [C0HM02](https://www.uniprot.org/uniprotkb/C0HM02) · Ensembl [ENSG00000027075](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000027075)

## Data

Gene col 377: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 377); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 377, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 377]; `tensor/DDL_lfc|DDL_z.npy` [377]; `embed/gene_vectors.npy` [377]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 377 or target_col == 377). Every well: [[PRKCH — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRKCH.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
