---
symbol: "HMSD"
type: "gene"
col: 13314
ensembl_id: "ENSG00000221887"
name: "histocompatibility minor serpin domain containing"
location: "18q22.1"
module: 14
arm: "+"
pooled_cpm: 2.17
n_lines_expressing: 24
n_dd_up: 30
n_dd_down: 0
n_dd_up_clean: 18
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 5
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# HMSD

*histocompatibility minor serpin domain containing* — 18q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (12 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.44× (z +12.7, q 3e-34, up in 14 of 16 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CD83]] (+0.69, fdr 1e-05), [[TMCC2]] (+0.64, fdr 1e-05), [[RIPK2]] (+0.60, fdr 1e-05); moves opposite to [[LRRC41]] (-0.57, fdr 1e-04), [[THAP4]] (-0.56, fdr 3e-04), [[TMEM11-DT]] (-0.54, fdr 6e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[IER3]] → it (grade B ⚠); 5 go from it, the strongest it → [[LRRC41]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 12 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13314.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.44×** | +12.7 | 3e-34 | 14/16 (PANC-1, J82, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.80×** | +10.6 | 8e-24 | 16/18 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.24×** | +10.1 | 9e-22 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.73×** | +9.6 | 1e-19 | 3/10 (LOX-IMVI, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **3.09×** | +8.2 | 2e-14 | 18/19 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.89×** | +7.7 | 9e-13 | 13/19 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.99×** | +7.4 | 1e-11 | 4/5 (Panc 03.27, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.69×** | +7.2 | 4e-11 | 14/19 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **2.77×** | +7.1 | 5e-11 | 15/17 (PANC-1, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.66×** | +7.1 | 5e-11 | 15/17 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.64×** | +6.8 | 6e-10 | 12/14 (NCI-H1573, A-427, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.42×** | +6.4 | 5e-09 | 17/19 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **3.01×** | +5.7 | 4e-07 | 2/6 (A-427, NCI-H460) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.71×** | +5.5 | 1e-06 | 3/16 (NCI-H2030, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.11×** | +5.4 | 2e-06 | 4/15 (PANC-1, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.54×** | +4.8 | 5e-05 | 1/14 (NCI-H1573) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.86×** | +4.5 | 2e-04 | 7/17 (A-427, PANC-1, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.75×** | +4.1 | 0.001 | 9/16 (RKO, HOP62, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.45×** | +3.8 | 0.003 | 2/19 (A-427, hTERT-HPNE) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | **1.69×** | +3.8 | 0.003 | 1/12 (LOX-IMVI) | inconsistent across doses | low cells (technical?) |
| [[Saquinavir (drug)]] 5 µM |  | **1.43×** | +3.7 | 0.005 | 1/15 (NCI-H460) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13314.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.891× | -3.3 | 0.43 | 4/20 (NCI-H1792, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | 0.649× | -3.2 | 0.43 | 4/19 (HOP62, SW 900, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13314. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 1.38 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 19.6× (z +12.7) | — |
| [[CFPAC-1 (line)]] | alt | 2.84 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.8× (z +9.6) | — |
| [[hTERT-HPNE (line)]] | wt | 5.77 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.6× (z +9.3) | — |
| [[J82 (line)]] | alt | 4.67 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.7× (z +12.2) | — |
| [[Panc 03.27 (line)]] | alt | 13.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.57× (z +8.7) | — |
| [[A-172 (line)]] | wt | 0.478 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.178 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.00 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.615 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.250 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.204 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.272 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.231 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.279 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.212 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.442 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.05 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.215 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.271 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.515 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.224 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.243 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.480 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.296 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.48 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.243 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.63 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.81 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.00 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.80 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.455 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.73 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.361 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.348 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.258 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.499 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.721 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.252 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 5.10 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.274 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.290 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.232 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13314), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CD83]] | +0.69 | +0.50 / +0.75 | both halves | 1e-05 |  |
| [[TMCC2]] | +0.64 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[RIPK2]] | +0.60 | +0.53 / +0.64 | both halves | 1e-05 |  |
| [[ADGRB2]] | +0.59 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[LRCH2]] | +0.56 | +0.41 / +0.59 | both halves | 4e-05 |  |
| [[BHLHE40]] | +0.56 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[PPP4R4]] | +0.56 | +0.46 / +0.52 | both halves | 2e-05 |  |
| [[TNFRSF9]] | +0.56 | +0.39 / +0.61 | both halves | 6e-05 |  |
| [[CYRIA]] | +0.55 | +0.32 / +0.52 | both halves | 1e-04 |  |
| [[RGS9]] | +0.55 | +0.30 / +0.61 | both halves | 2e-04 |  |
| [[STX11]] | +0.55 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[ELOVL4]] | +0.55 | +0.47 / +0.55 | both halves | 2e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LRRC41]] | -0.57 | -0.35 / -0.65 | both halves | 1e-04 |  |
| [[THAP4]] | -0.56 | -0.28 / -0.67 | both halves | 3e-04 |  |
| [[TMEM11-DT]] | -0.54 | -0.38 / -0.57 | both halves | 6e-05 |  |
| [[NHEJ1]] | -0.52 | -0.40 / -0.50 | both halves | 4e-05 |  |
| [[PRR14L]] | -0.52 | -0.35 / -0.59 | both halves | 1e-04 |  |
| [[APTX]] | -0.52 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[WDR81]] | -0.52 | -0.27 / -0.58 | both halves | 3e-04 |  |
| [[VPS51]] | -0.51 | -0.39 / -0.58 | both halves | 5e-05 |  |
| [[COX10]] | -0.50 | -0.41 / -0.46 | both halves | 4e-05 |  |
| [[HECTD1]] | -0.50 | -0.35 / -0.51 | both halves | 1e-04 |  |
| [[ZNF407]] | -0.50 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[HCG18]] | -0.49 | -0.36 / -0.50 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IER3]] | B | IER3 activity lowers HMSD's level | lines that do not express IER3 (5) vs lines expressing it (45) | 1.93× higher at baseline in the lines without IER3 | 0.033 | ⚠ within organs, on part of the lines; also absent: ARHGAP18, SLC2A1, SHB |
| [[TSPAN15]] | B | TSPAN15 activity lowers HMSD's level | lines that do not express TSPAN15 (15) vs lines expressing it (35) | 1.50× higher at baseline in the lines without TSPAN15 | 0.071 | ⚠ within organs, on part of the lines; also absent: RBM47, ENSG00000287306, JUP; maybe low, not absent |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LRRC41]] | B | HMSD activity raises LRRC41's level | lines that do not express HMSD (26) vs lines expressing it (24) | 1.14× lower at baseline in the lines without HMSD | 0.034 | ⚠ within organs, on part of the lines; also absent: LGSN, LRRN2, HEYL |
| [[ZMIZ2]] | B | HMSD activity lowers ZMIZ2's level | lines that do not express HMSD (26) vs lines expressing it (24) | 1.21× higher at baseline in the lines without HMSD | 0.044 | ⚠ within organs, on part of the lines; also absent: LGSN, LRRN2, HEYL |
| [[ANKAR]] | B | HMSD activity raises ANKAR's level | lines that do not express HMSD (26) vs lines expressing it (24) | 1.23× lower at baseline in the lines without HMSD | 0.055 | ⚠ within organs, on part of the lines; also absent: LGSN, LRRN2, HEYL |
| [[KPNA6]] | B | HMSD activity raises KPNA6's level | lines that do not express HMSD (26) vs lines expressing it (24) | 1.15× lower at baseline in the lines without HMSD | 0.066 | ⚠ within organs, on part of the lines; also absent: LGSN, LRRN2, HEYL |
| [[ZNF407]] | B | HMSD activity raises ZNF407's level | lines that do not express HMSD (26) vs lines expressing it (24) | 1.19× lower at baseline in the lines without HMSD | 0.089 | ⚠ within organs, on part of the lines; also absent: LGSN, LRRN2, HEYL |

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.546). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (26.2, 0.5); signed map (20.1, 22.1). **Vector** length 36.4, 7.52% of its response variance represented; |z| ≥ 3 in 391 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.8 | +10.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.2 | +7.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | +2.3 | +7.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.3 | +12.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.2 | +7.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.2 | +2.5 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.0 | +0.6 |
|  | [[Radotinib (drug)]] 5 µM |  | +0.8 | +0.6 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +0.8 | +2.2 |
| fall | [[5-Azacytidine (drug)]] 5 µM |  | -1.1 | -0.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.1 | -2.3 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.1 | -3.3 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.0 | +2.0 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.0 | -0.8 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.0 | -1.9 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -0.9 | -3.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -0.9 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | histocompatibility minor serpin domain containing |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q22.1 — chr18:63,949,301-63,981,774 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ACC-6, ACC6; previously C18orf53 |
| Gene groups (HGNC) | Minor histocompatibility antigens |
| Matched by | ensembl_id |

**Function**, from UniProt [A8MTL9](https://www.uniprot.org/uniprotkb/A8MTL9) (Serpin-like protein HMSD):

> Putative serine protease inhibitor.

**Summary**, from NCBI Gene [284293](https://www.ncbi.nlm.nih.gov/gene/284293):

> This gene encodes a serpin-domain containing protein that may function as a serine protease inhibitor. This gene is primarily expressed in cells of myeloid lineage. A polymorphism in this gene may result in the expression a splice variant that encodes a minor histocompatibility antigen. [provided by RefSeq, Oct 2010]

**Accessions** — [HGNC:23037](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23037) · Entrez [284293](https://www.ncbi.nlm.nih.gov/gene/284293) · UniProt [A8MTL9](https://www.uniprot.org/uniprotkb/A8MTL9) · Ensembl [ENSG00000221887](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000221887)

## Data

Gene col 13314: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13314); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13314, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13314]; `tensor/DDL_lfc|DDL_z.npy` [13314]; `embed/gene_vectors.npy` [13314]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13314 or target_col == 13314). Every well: [[HMSD — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HMSD.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
