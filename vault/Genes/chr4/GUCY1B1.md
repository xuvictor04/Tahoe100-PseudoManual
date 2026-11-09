---
symbol: "GUCY1B1"
type: "gene"
col: 703
ensembl_id: "ENSG00000061918"
name: "guanylate cyclase 1 soluble subunit beta 1"
location: "4q32.1"
module: 82
arm: "+"
pooled_cpm: 3.42
n_lines_expressing: 25
n_dd_up: 28
n_dd_down: 2
n_dd_up_clean: 18
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 2
tags: ["gene", "module/082"]
generated_by: "tahoemap"
---

# GUCY1B1

*guanylate cyclase 1 soluble subunit beta 1* — 4q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (10 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 3.62× (z +16.0, q 0e+00, up in 20 of 22 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.530× (z -5.6, q 1e-05, down in 9 of 22 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PDGFD]] (+0.66, fdr 7e-06), [[TMEM108]] (+0.64, fdr 1e-05), [[ZMAT4]] (+0.63, fdr 1e-05); moves opposite to [[COMMD1]] (-0.52, fdr 5e-05), [[CDKL3]] (-0.51, fdr 3e-04), [[LINS1]] (-0.51, fdr 2e-04).
> It is in [[Module 082]], a single-armed module (Muscle contraction).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[LPCAT2]] → it (grade B ⚠); 2 go from it, the strongest it → [[LPCAT2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 10 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 703.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **3.62×** | +16.0 | 0e+00 | 20/22 (NCI-H2347, hTERT-HPNE, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **5.96×** | +15.7 | 0e+00 | 21/21 (NCI-H2347, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **5.47×** | +14.9 | 0e+00 | 19/21 (NCI-H2347, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **5.17×** | +14.4 | 4e-45 | 19/20 (HOP62, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **4.73×** | +13.6 | 2e-40 | 20/22 (NCI-H2347, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.79×** | +11.3 | 2e-27 | 4/5 (A498, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.38×** | +10.7 | 9e-25 | 7/9 (A498, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.35×** | +10.6 | 2e-24 | 9/15 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **3.10×** | +9.9 | 2e-21 | 15/18 (NCI-H2347, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.18×** | +9.4 | 3e-19 | 2/5 (A498, CFPAC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **2.13×** | +6.6 | 2e-09 | 15/17 (NCI-H460, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Brivudine (drug)]] 5 µM |  | **3.89×** | +6.2 | 2e-08 | 15/20 (NCI-H2347, HEC-1-A, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.06×** | +6.1 | 5e-08 | 5/10 (HEC-1-A, HOP62, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.76×** | +5.0 | 3e-05 | 2/7 (A-172, CFPAC-1) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.80×** | +4.9 | 3e-05 | 1/12 (HS-578T) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.81×** | +4.9 | 4e-05 | 10/18 (HOP62, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Saquinavir (drug)]] 5 µM |  | **1.46×** | +4.7 | 8e-05 | 2/17 (NCI-H1792, NCI-H1573) | inconsistent across doses | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.65×** | +4.4 | 4e-04 | 5/18 (LOX-IMVI, HOP62, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.60×** | +3.9 | 0.002 | 7/17 (A498, NCI-H1792, …) | inconsistent across doses |  |
| [[Omeprazole (drug)]] 0.5 µM |  | **1.47×** | +3.4 | 0.018 | 1/18 (NCI-H1573) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.44×** | +3.2 | 0.033 | 8/21 (HOP62, LOX-IMVI, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 703.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.530×** | -5.6 | 1e-05 | 9/22 (A498, A-172, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.880× | -4.1 | 0.011 | 8/23 (NCI-H2030, CHP-212, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.677×** | -3.5 | 0.093 | 8/19 (A498, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dexamethasone (drug)]] 0.5 µM |  | 0.691× | -3.3 | 0.14 | 3/20 (A498, NCI-H1792, …) | inconsistent across doses | position effect removed |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.778× | -3.2 | 0.17 | 6/23 (A-172, RPMI-7951, …) | rises with dose |  |
| [[Fluvoxamine (drug)]] 0.5 µM |  | 0.710× | -3.1 | 0.21 | 2/22 (NCI-H661, HOP62) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.37 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 703. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 2.69 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 15.0× (z +9.0) | — |
| [[hTERT-HPNE (line)]] | wt | 5.26 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 8.78× (z +8.6) | — |
| [[NCI-H1573 (line)]] | alt | 2.56 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 18.3× (z +8.6) | — |
| [[A-172 (line)]] | wt | 6.25 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.77 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 38.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.514 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.363 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.219 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.853 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.261 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.219 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 6.12 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.26 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.209 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.27 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.225 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.239 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.304 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 5.47 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.241 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.236 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.202 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.231 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.73 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.213 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.181 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.97 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.926 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.83 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.487 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.392 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.210 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.251 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.13 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.281 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.243 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 6.21 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.60 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.72 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.191 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.239 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.193 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 703), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDGFD]] | +0.66 | +0.67 / +0.67 | both halves | 7e-06 |  |
| [[TMEM108]] | +0.64 | +0.67 / +0.56 | both halves | 1e-05 |  |
| [[ZMAT4]] | +0.63 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[ANOS1]] | +0.62 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[PPP2R2B]] | +0.62 | +0.58 / +0.65 | both halves | 7e-06 |  |
| [[MOXD1]] | +0.58 | +0.44 / +0.67 | both halves | 3e-05 |  |
| [[SSX1]] | +0.57 | +0.42 / +0.37 | both halves | 8e-05 |  |
| [[SYT11]] | +0.56 | +0.43 / +0.52 | both halves | 3e-05 | pathway: HALLMARK_IL2_STAT5_SIGNALING |
| [[SUSD4]] | +0.55 | +0.38 / +0.61 | both halves | 7e-05 |  |
| [[MPP1]] | +0.55 | +0.44 / +0.49 | both halves | 3e-05 |  |
| [[JAM3]] | +0.55 | +0.41 / +0.52 | both halves | 4e-05 |  |
| [[ANO5]] | +0.54 | +0.48 / +0.64 | both halves | 2e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COMMD1]] | -0.52 | -0.40 / -0.42 | both halves | 5e-05 |  |
| [[CDKL3]] | -0.51 | -0.33 / -0.29 | both halves | 3e-04 |  |
| [[LINS1]] | -0.51 | -0.30 / -0.43 | both halves | 2e-04 |  |
| [[UPF3A]] | -0.48 | -0.29 / -0.40 | both halves | 2e-04 |  |
| [[ITPA]] | -0.47 | -0.19 / -0.52 | ⚠ one half (not replicated) | 8e-04 | STRING 910 |
| [[DOHH]] | -0.47 | -0.29 / -0.35 | both halves | 2e-04 |  |
| [[LINC01004]] | -0.46 | -0.26 / -0.45 | both halves | 4e-04 |  |
| [[MTG2]] | -0.46 | -0.29 / -0.33 | both halves | 2e-04 |  |
| [[ACAD9]] | -0.46 | -0.25 / -0.38 | both halves | 4e-04 |  |
| [[ZFY]] | -0.46 | -0.29 / -0.40 | both halves | 3e-04 |  |
| [[FBXL9P]] | -0.45 | -0.32 / -0.36 | both halves | 2e-04 |  |
| [[NMNAT1]] | -0.45 | -0.30 / -0.34 | both halves | 2e-04 |  |
| [[UBE3B]] | -0.44 | -0.26 / -0.41 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LPCAT2]] | B | LPCAT2 activity raises GUCY1B1's level | lines that do not express LPCAT2 (9) vs lines expressing it (41) | 2.06× lower at baseline in the lines without LPCAT2 | 0.038 | ⚠ within organs, on part of the lines; also absent: E2F7, PARD3B |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LPCAT2]] | B | GUCY1B1 activity raises LPCAT2's level | lines that do not express GUCY1B1 (25) vs lines expressing it (25) | 1.76× lower at baseline in the lines without GUCY1B1 | 0.075 | ⚠ within organs, on part of the lines; also absent: FAP, STAC, SALL1 |
| [[ANO5]] | B | GUCY1B1 activity raises ANO5's level | lines that do not express GUCY1B1 (25) vs lines expressing it (25) | 1.51× lower at baseline in the lines without GUCY1B1 | 0.093 | ⚠ within organs, on part of the lines; also absent: FAP, STAC, SALL1 |

## Where it sits

- **Module**: [[Module 082]] — Muscle contraction; 55 genes; every member is in the + arm (projection on the module's main direction 0.544). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (41.7, 31.3); signed map (34.3, 33.6). **Vector** length 44.2, 9.13% of its response variance represented; |z| ≥ 3 in 578 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.2 | +16.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.1 | +9.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.0 | +11.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.7 | +10.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.2 | +9.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.7 | +6.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.6 | +3.2 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.1 | +2.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.0 | +3.9 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.7 | -4.1 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -1.4 | +0.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.3 | -2.0 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.1 | -0.5 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.0 | -1.2 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.0 | -3.3 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -0.9 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | guanylate cyclase 1 soluble subunit beta 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q32.1 — chr4:155,758,992-155,807,811 (+) |
| Ensembl biotype | protein_coding |
| Also known as | GC-SB3, GC-S-beta-1; previously GUC1B3, GUCY1B3 |
| Gene groups (HGNC) | Soluble guanylate cyclases |
| Hallmark sets | IL2_STAT5_SIGNALING |
| Reactome | 5 pathways, smallest: Nitric oxide stimulates guanylate cyclase; Smooth Muscle Contraction; Platelet homeostasis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q02153](https://www.uniprot.org/uniprotkb/Q02153) (Guanylate cyclase soluble subunit beta-1):

> Beta subunit of soluble guanylate cyclase (sGC), a key enzyme in nitric oxide (NO) signaling. sGC functions as a heterodimer consisting of one alpha and one beta subunit. It serves as the primary intracellular receptor for NO, which binds to a heme prosthetic group located on the beta subunit. Upon NO binding, sGC catalyzes the conversion of GTP into cyclic GMP (cGMP), thereby transmitting the NO signal into an ubiquitous intracellular second messenger.

**Summary**, from NCBI Gene [2983](https://www.ncbi.nlm.nih.gov/gene/2983):

> This gene encodes the beta subunit of the soluble guanylate cyclase (sGC), which catalyzes the conversion of GTP (guanosine triphosphate) to cGMP (cyclic guanosine monophosphate). The encoded protein contains an HNOX domain, which serves as a receptor for ligands such as nitric oxide, oxygen and nitrovasodilator drugs. Alternative splicing results in multiple transcript variants. [provided by RefSeq, May 2014]

**Accessions** — [HGNC:4687](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4687) · Entrez [2983](https://www.ncbi.nlm.nih.gov/gene/2983) · UniProt [Q02153](https://www.uniprot.org/uniprotkb/Q02153) · Ensembl [ENSG00000061918](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000061918)

## Data

Gene col 703: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 703); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 703, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 703]; `tensor/DDL_lfc|DDL_z.npy` [703]; `embed/gene_vectors.npy` [703]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 703 or target_col == 703). Every well: [[GUCY1B1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GUCY1B1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
