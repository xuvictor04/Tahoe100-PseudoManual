---
symbol: "ZFAND2A"
type: "gene"
col: 10920
ensembl_id: "ENSG00000178381"
name: "zinc finger AN1-type containing 2A"
location: "7p22.3"
module: 72
arm: "+"
pooled_cpm: 16.53
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 2
n_dd_up_clean: 10
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/072"]
generated_by: "tahoemap"
---

# ZFAND2A

*zinc finger AN1-type containing 2A* — 7p22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 17.3× (z +25.5, q 0e+00, up in 47 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.600× (z -6.4, q 7e-08, down in 35 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Tucidinostat (drug)]] 0.5 µM in 1 line (SW48 0.0510×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PCYT1A]] (+0.74, fdr 7e-06), [[DEDD2]] (+0.74, fdr 7e-06), [[ZNF581]] (+0.70, fdr 7e-06); moves opposite to [[SKA2]] (-0.61, fdr 2e-05), [[ECT2]] (-0.60, fdr 2e-05), [[NHLRC2]] (-0.58, fdr 3e-05).
> It is in [[Module 072]], a single-armed module (Degradation of DVL).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CRYAB]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10920.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **17.3×** | +25.5 | 0e+00 | 47/47 (LoVo, SW480, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **8.92×** | +18.4 | 0e+00 | 45/45 (HT-29, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **7.53×** | +18.0 | 0e+00 | 47/47 (LoVo, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **7.05×** | +17.4 | 0e+00 | 48/48 (LoVo, HOP62, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **16.9×** | +13.2 | 1e-37 | 36/36 (NCI-H2347, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled); position effect removed |
| [[Bortezomib (drug)]] 0.5 µM |  | **6.69×** | +9.8 | 1e-20 | 46/48 (NCI-H2347, CFPAC-1, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.40×** | +7.5 | 4e-12 | 31/40 (NCI-H460, SHP-77, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.64×** | +6.3 | 2e-08 | 30/44 (PANC-1, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.74×** | +5.0 | 4e-05 | 24/45 (LS 180, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~13% here) |
| [[Infigratinib (drug)]] 5 µM |  | **2.72×** | +4.7 | 2e-04 | 32/46 (HOP62, AsPC-1, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.49×** | +3.6 | 0.019 | 20/44 (A-172, LOX-IMVI, …) | two highest doses | cell-cycle shift (explains ~6% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.30×** | +3.3 | 0.038 | 22/48 (Hs 766T, A498, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | 1.41× | +3.0 | 0.10 | 14/47 (SW480, BT-474, …) | two highest doses | cell-cycle shift (explains ~15% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | 1.79× | +3.0 | 0.11 | 18/39 (HS-578T, SK-MEL-2, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10920.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Tucidinostat (drug)]] 0.5 µM in 1 line (SW48 0.0510×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.600×** | -6.4 | 7e-08 | 35/48 (A498, NCI-H2347, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.601×** | -4.5 | 0.002 | 30/47 (SW48, KATO III, …) | rises with dose | cell-cycle shift (explains ~4% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, +0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10920. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 12.6 | 7 (3 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 13.1× (z +13.8) | — |
| [[A-172 (line)]] | wt | 20.3 | 5 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 22.1× (z +17.9) | — |
| [[CFPAC-1 (line)]] | alt | 17.7 | 5 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 11.6× (z +12.4) | — |
| [[HT-29 (line)]] | alt | 13.8 | 5 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 50.2× (z +18.1) | — |
| [[NCI-H2347 (line)]] | alt | 16.2 | 5 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 10.3× (z +14.2) | — |
| [[SW1417 (line)]] | alt | 19.1 | 5 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 14.4× (z +14.1) | — |
| [[A-427 (line)]] | wt | 9.16 | 4 | 0 | [[Auranofin (drug)]] 5 µM 42.3× (z +17.3) | — |
| [[A498 (line)]] | wt | 54.1 | 4 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 8.70× (z +12.1) | — |
| [[H4 (line)]] | wt | 32.8 | 4 | 0 | [[Auranofin (drug)]] 5 µM 22.9× (z +15.2) | — |
| [[HEC-1-A (line)]] | alt | 6.95 | 4 | 0 | [[Auranofin (drug)]] 5 µM 43.5× (z +17.0) | — |
| [[HOP62 (line)]] | alt | 8.98 | 4 | 0 | [[Auranofin (drug)]] 5 µM 39.6× (z +19.3) | — |
| [[HS-578T (line)]] | alt | 19.3 | 4 | 0 | [[Auranofin (drug)]] 5 µM 9.39× (z +11.9) | — |
| [[J82 (line)]] | alt | 11.7 | 4 | 0 | [[Bortezomib (drug)]] 0.05 µM 9.07× (z +10.5) | — |
| [[KATO III (line)]] | alt | 20.9 | 4 | 0 | [[Bortezomib (drug)]] 0.05 µM 14.0× (z +13.2) | — |
| [[LoVo (line)]] | wt | 11.4 | 4 | 0 | [[Auranofin (drug)]] 5 µM 59.2× (z +21.1) | — |
| [[LS 180 (line)]] | wt | 14.3 | 4 | 0 | [[Bortezomib (drug)]] 0.05 µM 13.4× (z +11.6) | — |
| [[NCI-H2030 (line)]] | alt | 15.1 | 4 | 0 | [[Auranofin (drug)]] 5 µM 9.80× (z +11.5) | — |
| [[Panc 03.27 (line)]] | alt | 12.5 | 4 | 0 | [[Auranofin (drug)]] 5 µM 17.2× (z +12.9) | — |
| [[PANC-1 (line)]] | alt | 10.3 | 4 | 0 | [[Auranofin (drug)]] 5 µM 25.8× (z +17.5) | — |
| [[SK-MEL-2 (line)]] | alt | 13.4 | 4 | 0 | [[Auranofin (drug)]] 5 µM 38.8× (z +16.5) | — |
| [[SNU-423 (line)]] | alt | 12.3 | 4 | 0 | [[Auranofin (drug)]] 5 µM 31.1× (z +16.5) | — |
| [[SW480 (line)]] | alt | 13.5 | 4 | 0 | [[Auranofin (drug)]] 5 µM 31.0× (z +19.8) | — |
| [[AsPC-1 (line)]] | alt | 57.9 | 3 | 0 | [[Auranofin (drug)]] 5 µM 8.09× (z +14.3) | — |
| [[Hs 766T (line)]] | wt | 20.6 | 3 | 0 | [[Auranofin (drug)]] 5 µM 8.69× (z +11.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 10.5 | 3 | 0 | [[Auranofin (drug)]] 5 µM 44.0× (z +16.2) | — |
| [[NCI-H1792 (line)]] | alt | 33.2 | 3 | 0 | [[Bortezomib (drug)]] 0.05 µM 5.63× (z +9.9) | — |
| [[RPMI-7951 (line)]] | alt | 15.4 | 3 | 0 | [[Auranofin (drug)]] 5 µM 19.7× (z +13.9) | — |
| [[SW 900 (line)]] | alt | 25.1 | 3 | 0 | [[Auranofin (drug)]] 5 µM 15.2× (z +14.1) | — |
| [[C32 (line)]] | wt | 6.94 | 2 | 0 | [[Auranofin (drug)]] 5 µM 71.5× (z +14.5) | — |
| [[HCT15 (line)]] | alt | 13.8 | 2 | 0 | [[Auranofin (drug)]] 5 µM 17.5× (z +11.0) | — |
| [[LOX-IMVI (line)]] | wt | 7.11 | 2 | 0 | [[Auranofin (drug)]] 5 µM 26.8× (z +12.8) | — |
| [[SW48 (line)]] | wt | 11.2 | 1 | 1 | [[Auranofin (drug)]] 5 µM 34.9× (z +11.4) | [[Tucidinostat (drug)]] 0.5 µM 0.0510× (z -9.5) |
| [[A549 (line)]] | wt | 11.2 | 1 | 0 | [[Bortezomib (drug)]] 0.05 µM 6.91× (z +8.5) | — |
| [[AN3 CA (line)]] | alt | 17.4 | 1 | 0 | [[Auranofin (drug)]] 5 µM 17.0× (z +8.5) | — |
| [[BT-474 (line)]] | alt | 10.3 | 1 | 0 | [[Auranofin (drug)]] 5 µM 70.4× (z +17.9) | — |
| [[C-33 A (line)]] | alt | 6.03 | 1 | 0 | [[Auranofin (drug)]] 5 µM 39.5× (z +11.0) | — |
| [[HepG2_C3A (line)]] | wt | 39.5 | 1 | 0 | [[Auranofin (drug)]] 5 µM 5.42× (z +10.0) | — |
| [[hTERT-HPNE (line)]] | wt | 10.2 | 1 | 0 | [[Auranofin (drug)]] 5 µM 21.6× (z +11.1) | — |
| [[NCI-H23 (line)]] | alt | 10.3 | 1 | 0 | [[Auranofin (drug)]] 5 µM 30.8× (z +15.4) | — |
| [[RKO (line)]] | wt | 7.92 | 1 | 0 | [[Auranofin (drug)]] 5 µM 28.3× (z +12.6) | — |
| [[SHP-77 (line)]] | alt | 20.9 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 8.12× (z +9.9) ⚠ toxic | — |
| [[SNU-1 (line)]] | wt | 7.10 | 1 | 0 | [[Auranofin (drug)]] 5 µM 31.3× (z +10.0) | — |
| [[SW 1271 (line)]] | alt | 14.0 | 1 | 0 | [[Auranofin (drug)]] 5 µM 75.1× (z +9.5) | — |
| [[CHP-212 (line)]] | wt | 9.43 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.16 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 20.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10920), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PCYT1A]] | +0.74 | +0.77 / +0.64 | both halves | 7e-06 |  |
| [[DEDD2]] | +0.74 | +0.76 / +0.68 | both halves | 7e-06 |  |
| [[ZNF581]] | +0.70 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[BRF2]] | +0.69 | +0.72 / +0.62 | both halves | 7e-06 |  |
| [[MRPL18]] | +0.69 | +0.60 / +0.75 | both halves | 7e-06 |  |
| [[ANKRD39]] | +0.69 | +0.59 / +0.72 | both halves | 7e-06 |  |
| [[TMEM208]] | +0.66 | +0.57 / +0.66 | both halves | 1e-05 |  |
| [[ZNF771]] | +0.66 | +0.66 / +0.62 | both halves | 7e-06 |  |
| [[TANGO2]] | +0.66 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[BAHD1]] | +0.66 | +0.57 / +0.60 | both halves | 9e-06 |  |
| [[FLYWCH1]] | +0.64 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[SLC51A]] | +0.64 | +0.54 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SKA2]] | -0.61 | -0.64 / -0.47 | both halves | 2e-05 |  |
| [[ECT2]] | -0.60 | -0.47 / -0.61 | both halves | 2e-05 |  |
| [[NHLRC2]] | -0.58 | -0.44 / -0.60 | both halves | 3e-05 |  |
| [[H2AZ2]] | -0.58 | -0.62 / -0.48 | both halves | 2e-05 |  |
| [[VMA21]] | -0.56 | -0.57 / -0.50 | both halves | 1e-05 |  |
| [[SEMA3C]] | -0.56 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[SF3B3]] | -0.55 | -0.45 / -0.62 | both halves | 3e-05 |  |
| [[CBX5]] | -0.54 | -0.48 / -0.49 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CRYAB]] | B | CRYAB activity raises ZFAND2A's level | lines that do not express CRYAB (32) vs lines expressing it (18) | 1.55× lower at baseline in the lines without CRYAB | 0.091 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CHL1, S100A1, AMBP |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 072]] — Degradation of DVL; 69 genes; every member is in the + arm (projection on the module's main direction 0.748). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-17.0, -7.7); signed map (-25.2, -25.7). **Vector** length 113, 32.3% of its response variance represented; |z| ≥ 3 in 936 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +12.3 | +18.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +12.1 | +25.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +11.5 | +18.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +10.5 | +17.4 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +8.2 | +13.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +5.9 | +9.8 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.4 | +2.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.2 | +2.0 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -6.9 | +0.3 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -6.6 | -1.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.8 | -2.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.5 | -6.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.4 | +0.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.9 | +1.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.5 | -2.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.3 | -1.4 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.3 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger AN1-type containing 2A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p22.3 — chr7:1,152,071-1,160,759 (-) |
| Ensembl biotype | protein_coding |
| Also known as | AIRAP |
| Gene groups (HGNC) | Zinc fingers AN1-type |
| Matched by | ensembl_id |

UniProt [Q8N6M9](https://www.uniprot.org/uniprotkb/Q8N6M9) carries no function annotation.

**Summary**, from NCBI Gene [90637](https://www.ncbi.nlm.nih.gov/gene/90637):

> Predicted to enable zinc ion binding activity. Predicted to be involved in proteasome-mediated ubiquitin-dependent protein catabolic process and protein targeting to ER. Predicted to act upstream of or within cellular response to arsenic-containing substance and positive regulation of proteasomal ubiquitin-dependent protein catabolic process. Predicted to be located in nucleus. Predicted to be part of proteasome complex. Predicted to be active in endoplasmic reticulum. [provided by Alliance of …

**Accessions** — [HGNC:28073](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28073) · Entrez [90637](https://www.ncbi.nlm.nih.gov/gene/90637) · UniProt [Q8N6M9](https://www.uniprot.org/uniprotkb/Q8N6M9) · Ensembl [ENSG00000178381](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000178381)

## Data

Gene col 10920: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10920); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10920, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10920]; `tensor/DDL_lfc|DDL_z.npy` [10920]; `embed/gene_vectors.npy` [10920]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10920 or target_col == 10920). Every well: [[ZFAND2A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZFAND2A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
