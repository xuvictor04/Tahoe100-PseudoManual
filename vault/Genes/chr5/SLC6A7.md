---
symbol: "SLC6A7"
type: "gene"
col: 222
ensembl_id: "ENSG00000011083"
name: "solute carrier family 6 member 7"
location: "5q32"
module: 14
arm: "+"
pooled_cpm: 2.14
n_lines_expressing: 23
n_dd_up: 16
n_dd_down: 0
n_dd_up_clean: 8
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 5
direction_downstream: 10
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# SLC6A7

*solute carrier family 6 member 7* — 5q32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.92× (z +10.5, q 7e-23, up in 11 of 13 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 0.5 µM in 1 line (NCI-H460 0.116×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IL32]] (+0.70, fdr 7e-06), [[TNFAIP2]] (+0.65, fdr 1e-05), [[STAP2]] (+0.63, fdr 1e-05); moves opposite to [[BCAP31]] (-0.54, fdr 1e-05), [[TCF3]] (-0.51, fdr 6e-05), [[NTAQ1]] (-0.51, fdr 3e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[ABCC9]] → it (grade B ⚠); 10 go from it, the strongest it → [[BCL3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 8 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 222.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.92×** | +10.5 | 7e-23 | 11/13 (HOP62, A-172, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.61×** | +8.0 | 5e-13 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.57×** | +6.8 | 2e-09 | 1/3 (NCI-H460) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **3.60×** | +6.7 | 4e-09 | 13/16 (HOP62, A-172, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **3.28×** | +6.2 | 7e-08 | 4/5 (HOP62, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.11×** | +6.1 | 8e-08 | 1/5 (AsPC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.07×** | +5.6 | 2e-06 | 2/13 (hTERT-HPNE, A-172) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.77×** | +4.3 | 1e-03 | 7/18 (Panc 03.27, hTERT-HPNE, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.21×** | +4.1 | 0.002 | 7/14 (A-172, SW1417, …) | rises with dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.67×** | +3.9 | 0.005 | 3/19 (SW1417, Panc 03.27, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.79×** | +3.8 | 0.009 | 0/4 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.04×** | +3.7 | 0.010 | 2/7 (NCI-H460, Panc 03.27) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.90×** | +3.5 | 0.022 | 0/8 | top dose only | cell-cycle shift (explains ~7% here) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.89×** | +3.4 | 0.023 | 0/8 | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.47×** | +3.3 | 0.034 | 0/4 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.50×** | +3.1 | 0.068 | 0/18 | top dose only |  |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 0.5 µM in 1 line (NCI-H460 0.116×).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 222. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 3.52 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 20.9× (z +13.0) | — |
| [[A-172 (line)]] | wt | 1.18 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 60.8× (z +11.3) | — |
| [[NCI-H460 (line)]] | wt | 25.7 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.116× (z -10.2) |
| [[A-427 (line)]] | wt | 0.196 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.241 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.330 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.533 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 4.61 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.279 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.283 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.265 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.386 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.333 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.356 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.333 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.565 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.273 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.711 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.393 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.956 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.97 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.702 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.674 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.433 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.786 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.38 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.830 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.351 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.599 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.228 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.48 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.256 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.485 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.370 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.253 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.279 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 5.38 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.268 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.323 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.259 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.854 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.320 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.940 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.331 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.238 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 222), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IL32]] | +0.70 | +0.68 / +0.62 | both halves | 7e-06 |  |
| [[TNFAIP2]] | +0.65 | +0.49 / +0.65 | both halves | 1e-05 |  |
| [[STAP2]] | +0.63 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[KMO]] | +0.63 | +0.55 / +0.60 | both halves | 1e-05 | pathway: Metabolism of amino acids and derivatives |
| [[BCL3]] | +0.62 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[IGSF1]] | +0.61 | +0.49 / +0.65 | both halves | 1e-05 |  |
| [[C1QTNF1-AS1]] | +0.61 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[SLC2A6]] | +0.60 | +0.55 / +0.59 | both halves | 1e-05 | pathway: SLC-mediated transmembrane transport |
| [[BTN2A2]] | +0.60 | +0.49 / +0.62 | both halves | 1e-05 |  |
| [[STAT5A]] | +0.60 | +0.46 / +0.60 | both halves | 2e-05 |  |
| [[TNFAIP6]] | +0.59 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[LINC02605]] | +0.59 | +0.47 / +0.66 | both halves | 2e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BCAP31]] | -0.54 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[TCF3]] | -0.51 | -0.56 / -0.39 | both halves | 6e-05 |  |
| [[NTAQ1]] | -0.51 | -0.49 / -0.45 | both halves | 3e-05 |  |
| [[MAPK1]] | -0.51 | -0.57 / -0.35 | both halves | 1e-04 |  |
| [[TPP2]] | -0.50 | -0.43 / -0.50 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 1, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ABCC9]] | B | ABCC9 activity raises SLC6A7's level | lines that do not express ABCC9 (28) vs lines expressing it (22) | 1.44× lower at baseline in the lines without ABCC9 | 0.074 | ⚠ within organs, on part of the lines; also absent: WNT5A, PDGFRB, CCL3; maybe low, not absent |
| [[MARCOL]], [[SPINK13]] | C | MARCOL, SPINK13 activity raises SLC6A7's level | lines that do not express MARCOL, SPINK13 (45) vs lines expressing them (5) | 2.56× lower at baseline in the lines without MARCOL, SPINK13 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TBXT, ENSG00000230258, ENSG00000230975; co-absent with the target; co-absent genes |
| [[CXCL3]] | C | CXCL3 activity raises SLC6A7's level | lines that do not express CXCL3 (14) vs lines expressing it (36) | 1.70× lower at baseline in the lines without CXCL3 | 0.056 | ⚠ within organs, on part of the lines; also absent: MGLL, SPTLC3, PCED1B; co-absent with the target |
| [[IL6]] | C | IL6 activity raises SLC6A7's level | lines that do not express IL6 (32) vs lines expressing it (18) | 1.57× lower at baseline in the lines without IL6 | 0.071 | ⚠ within organs, on part of the lines; also absent: ENSG00000232949, STEAP1B-AS1, G0S2; co-absent with the target |
| [[TNFAIP2]] | C | TNFAIP2 activity raises SLC6A7's level | lines that do not express TNFAIP2 (22) vs lines expressing it (28) | 1.48× lower at baseline in the lines without TNFAIP2 | 0.090 | ⚠ within organs, on part of the lines; also absent: ADAMTS16, LINC02057, DEPP1; co-absent with the target |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 4, C 6.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BCL3]] | B | SLC6A7 activity raises BCL3's level | lines that do not express SLC6A7 (27) vs lines expressing it (23) | 1.56× lower at baseline in the lines without SLC6A7 | 0.041 | ⚠ within organs, on part of the lines; also absent: IL1B, UGT1A6, UGT1A9 |
| [[SLC9A8]] | B | SLC6A7 activity raises SLC9A8's level | lines that do not express SLC6A7 (27) vs lines expressing it (23) | 1.31× lower at baseline in the lines without SLC6A7 | 0.090 | ⚠ within organs, on part of the lines; also absent: IL1B, UGT1A6, UGT1A9 |
| [[LGALS3]] | B | SLC6A7 activity raises LGALS3's level | lines that do not express SLC6A7 (27) vs lines expressing it (23) | 2.07× lower at baseline in the lines without SLC6A7 | 0.096 | ⚠ within organs, on part of the lines; also absent: IL1B, UGT1A6, UGT1A9 |
| [[CASP10]] | B | SLC6A7 activity raises CASP10's level | lines that do not express SLC6A7 (27) vs lines expressing it (23) | 2.08× lower at baseline in the lines without SLC6A7 | 0.097 | ⚠ within organs, on part of the lines; also absent: IL1B, UGT1A6, UGT1A9 |
| [[LINC02577]] | C | SLC6A7 activity raises LINC02577's level | lines that do not express SLC6A7 (27) vs lines expressing it (23) | 3.69× lower at baseline in the lines without SLC6A7 | 0.008 | ⚠ within organs, on part of the lines; also absent: IL1B, UGT1A6, UGT1A9; co-absent with the target |
| [[CXCL3]] | C | SLC6A7 activity raises CXCL3's level | lines that do not express SLC6A7 (27) vs lines expressing it (23) | 2.19× lower at baseline in the lines without SLC6A7 | 0.029 | ⚠ within organs, on part of the lines; also absent: IL1B, UGT1A6, UGT1A9; co-absent with the target |
| [[ACKR3]] | C | SLC6A7 activity raises ACKR3's level | lines that do not express SLC6A7 (27) vs lines expressing it (23) | 1.74× lower at baseline in the lines without SLC6A7 | 0.041 | ⚠ within organs, on part of the lines; also absent: IL1B, UGT1A6, UGT1A9; co-absent with the target |
| [[TNFAIP2]] | C | SLC6A7 activity raises TNFAIP2's level | lines that do not express SLC6A7 (27) vs lines expressing it (23) | 2.50× lower at baseline in the lines without SLC6A7 | 0.054 | ⚠ within organs, on part of the lines; also absent: IL1B, UGT1A6, UGT1A9; co-absent with the target |
| [[IL6]] | C | SLC6A7 activity raises IL6's level | lines that do not express SLC6A7 (27) vs lines expressing it (23) | 2.56× lower at baseline in the lines without SLC6A7 | 0.079 | ⚠ within organs, on part of the lines; also absent: IL1B, UGT1A6, UGT1A9; co-absent with the target |
| [[IRAG2]] | C | SLC6A7 activity raises IRAG2's level | lines that do not express SLC6A7 (27) vs lines expressing it (23) | 1.78× lower at baseline in the lines without SLC6A7 | 0.083 | ⚠ within organs, on part of the lines; also absent: IL1B, UGT1A6, UGT1A9; co-absent with the target |

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.717). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (25.7, 3.8); signed map (43.3, 9.1). **Vector** length 33.3, 7.14% of its response variance represented; |z| ≥ 3 in 385 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +3.3 | +10.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | +2.6 | +6.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.1 | +4.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.1 | +6.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.1 | +6.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.2 | +3.1 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.1 | +1.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.0 | +2.8 |
|  | [[Amsacrine (drug)]] 5 µM |  | +0.9 | +2.1 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.2 | -1.8 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.2 | -2.1 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.1 | -2.3 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.0 | -0.3 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -0.9 | -0.8 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -0.8 | -1.1 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.8 | -2.3 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.8 | -2.5 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -0.7 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 6 member 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q32 — chr5:150,190,062-150,222,788 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PROT |
| Gene groups (HGNC) | Solute carrier family 6 |
| Reactome | 5 pathways, smallest: Creatine metabolism; SLC-mediated transport of neurotransmitters; SLC-mediated transmembrane transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99884](https://www.uniprot.org/uniprotkb/Q99884) (Sodium-dependent proline transporter):

> Brain specific sodium (and chloride)-dependent proline transporter. Terminates the action of proline by its high affinity sodium-dependent reuptake into presynaptic terminals (Probable).

**Summary**, from NCBI Gene [6534](https://www.ncbi.nlm.nih.gov/gene/6534):

> This gene is a member of the gamma-aminobutyric acid (GABA) neurotransmitter gene family and encodes a high-affinity mammalian brain L-proline transporter protein. This transporter protein differs from other sodium-dependent plasma membrane carriers by its pharmacological specificity, kinetic properties, and ionic requirements. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:11054](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11054) · Entrez [6534](https://www.ncbi.nlm.nih.gov/gene/6534) · UniProt [Q99884](https://www.uniprot.org/uniprotkb/Q99884) · Ensembl [ENSG00000011083](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000011083)

## Data

Gene col 222: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 222); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 222, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 222]; `tensor/DDL_lfc|DDL_z.npy` [222]; `embed/gene_vectors.npy` [222]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 222 or target_col == 222). Every well: [[SLC6A7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC6A7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
