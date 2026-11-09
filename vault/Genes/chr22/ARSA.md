---
symbol: "ARSA"
type: "gene"
col: 1918
ensembl_id: "ENSG00000100299"
name: "arylsulfatase A"
location: "22q13.33"
module: 50
arm: "+"
pooled_cpm: 2.94
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 13
n_dd_up_clean: 9
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/050"]
generated_by: "tahoemap"
---

# ARSA

*arylsulfatase A* — 22q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.15× (z +13.1, q 2e-36, up in 5 of 6 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 1.96× (z +6.4, q 1e-08, up in 18 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.467× (z -10.3, q 5e-22, down in 25 of 34 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GM2A]] (+0.69, fdr 1e-05), [[RNASEH2C]] (+0.67, fdr 1e-05), [[TMEM276]] (+0.63, fdr 1e-05); moves opposite to [[ICE2]] (-0.57, fdr 3e-05), [[ZNF286B]] (-0.55, fdr 5e-05), [[CDKL1]] (-0.54, fdr 1e-04).
> It is in [[Module 050]], a single-armed module (Extracellular matrix organization).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[PCSK1N]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 8 with an alert ⚠. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1918.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.15×** | +13.1 | 2e-36 | 5/6 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.79×** | +12.8 | 7e-35 | 15/15 (KATO III, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.38×** | +7.7 | 3e-12 | 5/7 (PANC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **2.01×** | +6.7 | 3e-09 | 21/46 (SW480, LS 180, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.96×** | +6.4 | 1e-08 | 18/42 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.45×** | +5.0 | 5e-05 | 8/45 (NCI-H2030, A-172, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.63×** | +4.7 | 2e-04 | 12/44 (LS 180, LoVo, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.66×** | +4.6 | 2e-04 | 5/18 (A498, HS-578T, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.54×** | +4.1 | 0.002 | 7/30 (CFPAC-1, SNU-423, …) | inconsistent across doses | low cells (technical?) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.54×** | +4.1 | 0.002 | 7/18 (HEC-1-A, SHP-77, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~2% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.55×** | +4.0 | 0.003 | 11/36 (LS 180, NCI-H460, …) | top dose only | cell-cycle shift (explains ~24% here); position effect removed |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.15×** | +3.7 | 0.008 | 1/5 (NCI-H2030) | top dose only | noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.04×** | +3.7 | 0.008 | 3/14 (LS 180, NCI-H2347, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.45×** | +3.6 | 0.014 | 2/45 (SW480, KATO III) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.45×** | +3.6 | 0.014 | 5/42 (NCI-H460, A-427, …) | two highest doses | cell-cycle shift (explains ~10% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.26×** | +3.1 | 0.060 | 6/44 (NCI-H460, A549, …) | top dose only | position effect removed |
| [[Saquinavir (drug)]] 0.05 µM |  | **1.37×** | +3.0 | 0.088 | 1/38 (LoVo) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, none with an alert. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1918.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.467×** | -10.3 | 5e-22 | 25/34 (PANC-1, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.480×** | -7.0 | 7e-10 | 21/31 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.514×** | -6.1 | 2e-07 | 21/41 (PANC-1, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.551×** | -5.7 | 2e-06 | 21/43 (A-172, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.597×** | -4.9 | 1e-04 | 15/46 (J82, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **0.638×** | -4.1 | 0.004 | 17/40 (HS-578T, NCI-H460, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.660×** | -4.0 | 0.006 | 11/44 (RKO, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.679×** | -3.7 | 0.016 | 16/40 (LoVo, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.669×** | -3.6 | 0.018 | 11/41 (A498, HepG2/C3A, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.692×** | -3.5 | 0.024 | 11/44 (LOX-IMVI, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.678×** | -3.5 | 0.024 | 11/41 (KATO III, SW1417, …) | inconsistent across doses |  |
| [[Tadalafil (drug)]] 5 µM |  | **0.699×** | -3.3 | 0.047 | 14/42 (NCI-H23, SW1417, …) | top dose only |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.723×** | -3.1 | 0.086 | 9/45 (HT-29, LOX-IMVI, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.32 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1918. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 5.68 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.163× (z -9.4) |
| [[NCI-H2030 (line)]] | alt | 6.92 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -9.3) |
| [[NCI-H460 (line)]] | wt | 3.20 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0928× (z -9.5) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.224× (z -8.8) |
| [[A498 (line)]] | wt | 3.23 | 0 | 1 | — | [[Bortezomib (drug)]] 0.05 µM 0.0746× (z -9.8) |
| [[C32 (line)]] | wt | 4.13 | 0 | 1 | — | [[Cytarabine (hydrochloride) (drug)]] 0.05 µM 0.0457× (z -9.1) |
| [[LoVo (line)]] | wt | 2.87 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0814× (z -8.8) |
| [[PANC-1 (line)]] | alt | 4.37 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -9.7) |
| [[A-172 (line)]] | wt | 2.88 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.43 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.82 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.82 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.25 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.51 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.95 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.68 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.78 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.02 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.01 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.26 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.84 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.20 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.04 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.72 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.07 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.43 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.56 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.30 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.20 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.48 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.38 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1918), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GM2A]] | +0.69 | +0.66 / +0.52 | both halves | 1e-05 | pathway: Glycosphingolipid catabolism; STRING 483 |
| [[RNASEH2C]] | +0.67 | +0.52 / +0.65 | both halves | 1e-05 |  |
| [[TMEM276]] | +0.63 | +0.66 / +0.52 | both halves | 1e-05 |  |
| [[ROGDI]] | +0.63 | +0.57 / +0.50 | both halves | 1e-05 |  |
| [[IGSF8]] | +0.62 | +0.58 / +0.48 | both halves | 2e-05 |  |
| [[NAGA]] | +0.61 | +0.67 / +0.46 | both halves | 2e-05 |  |
| [[NOMO1]] | +0.60 | +0.64 / +0.34 | both halves | 1e-04 |  |
| [[ZDHHC12]] | +0.60 | +0.57 / +0.47 | both halves | 2e-05 |  |
| [[CTXN1]] | +0.60 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[NPTN]] | +0.59 | +0.56 / +0.42 | both halves | 4e-05 |  |
| [[CTSF]] | +0.59 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[RTL8C]] | +0.58 | +0.54 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ICE2]] | -0.57 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[ZNF286B]] | -0.55 | -0.56 / -0.40 | both halves | 5e-05 |  |
| [[CDKL1]] | -0.54 | -0.52 / -0.35 | both halves | 1e-04 |  |
| [[ST7L]] | -0.52 | -0.42 / -0.41 | both halves | 4e-05 |  |
| [[DCPS]] | -0.52 | -0.47 / -0.37 | both halves | 9e-05 |  |
| [[SLF2]] | -0.50 | -0.40 / -0.45 | both halves | 5e-05 |  |
| [[MYSM1]] | -0.50 | -0.44 / -0.40 | both halves | 5e-05 |  |
| [[LZIC]] | -0.50 | -0.45 / -0.28 | both halves | 3e-04 |  |
| [[TAF1]] | -0.50 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[C10orf88]] | -0.49 | -0.55 / -0.28 | both halves | 3e-04 |  |
| [[MDC1]] | -0.49 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[FBXO4]] | -0.49 | -0.38 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PCSK1N]] | B | PCSK1N activity lowers ARSA's level | lines that do not express PCSK1N (21) vs lines expressing it (29) | 1.11× higher at baseline in the lines without PCSK1N | 0.029 | ⚠ within organs, on part of the lines; also absent: MAP6, CERS4, CACNG4 |
| [[C1QL1]] | B | C1QL1 activity raises ARSA's level | lines that do not express C1QL1 (22) vs lines expressing it (28) | 1.27× lower at baseline in the lines without C1QL1 | 0.059 | ⚠ within organs, on part of the lines; also absent: CPEB1, PDZD4, BARX1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 050]] — Extracellular matrix organization; 92 genes; every member is in the + arm (projection on the module's main direction 0.619). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-4.0, -22.1); signed map (-37.3, 15.1). **Vector** length 44.8, 5.10% of its response variance represented; |z| ≥ 3 in 1,024 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.4 | +12.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | +2.4 | +6.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.4 | +13.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.3 | +6.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.0 | +7.7 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.4 | +3.7 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.3 | +2.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.2 | +3.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.1 | +2.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.1 | +2.7 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.8 | -7.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.6 | -10.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.6 | -6.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -1.8 | -3.5 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.5 | -2.0 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.5 | -0.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.3 | -2.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.2 | -4.1 |
|  | [[Adenosine (drug)]] 0.5 µM |  | -1.0 | -1.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -0.9 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | arylsulfatase A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.33 — chr22:50,622,754-50,628,173 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ASA |
| Gene groups (HGNC) | Sulfatases |
| Reactome | 8 pathways, smallest: The activation of arylsulfatases; Glycosphingolipid catabolism; Glycosphingolipid metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [P15289](https://www.uniprot.org/uniprotkb/P15289) (Arylsulfatase A):

> Lysosomal enzyme that catalyzes the hydrolysis of cerebroside-3-sulfate (N-acyl-1-beta-D-(3-O-sulfo)-galactosyl-sphing-4-enine) into cerebroside and sulfate, a reaction that requires the activator protein saposin B. Also involved in the catabolism of other sulfoglycosphingolipids such as SB1a and SM3 (beta-D-3-sulfogalactosyl-(1->4)-beta-D-glucosyl-(1<->1')-N-acylsphing-4-enine) (By similarity).

**Summary**, from NCBI Gene [410](https://www.ncbi.nlm.nih.gov/gene/410):

> The protein encoded by this gene hydrolyzes cerebroside sulfate to cerebroside and sulfate. Defects in this gene lead to metachromatic leucodystrophy (MLD), a progressive demyelination disease which results in a variety of neurological symptoms and ultimately death. Alternatively spliced transcript variants have been described for this gene. [provided by RefSeq, Dec 2010]

**Accessions** — [HGNC:713](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:713) · Entrez [410](https://www.ncbi.nlm.nih.gov/gene/410) · UniProt [P15289](https://www.uniprot.org/uniprotkb/P15289) · Ensembl [ENSG00000100299](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100299)

## Data

Gene col 1918: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1918); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1918, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1918]; `tensor/DDL_lfc|DDL_z.npy` [1918]; `embed/gene_vectors.npy` [1918]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1918 or target_col == 1918). Every well: [[ARSA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARSA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
