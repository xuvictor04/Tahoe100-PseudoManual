---
symbol: "COLEC12"
type: "gene"
col: 8147
ensembl_id: "ENSG00000158270"
name: "collectin subfamily member 12"
location: "18p11.32"
module: 61
arm: "+"
pooled_cpm: 4.19
n_lines_expressing: 25
n_dd_up: 33
n_dd_down: 3
n_dd_up_clean: 24
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 8
direction_downstream: 2
tags: ["gene", "module/061"]
generated_by: "tahoemap"
---

# COLEC12

*collectin subfamily member 12* — 18p11.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 33 drug-doses (9 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 3.49× (z +16.0, q 0e+00, up in 15 of 20 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.870× (z -4.6, q 0.002, down in 4 of 21 measured lines) ⚠ position not correctable. The strongest without an alert is [[Triamcinolone (drug)]] 0.5 µM: 0.609× (z -4.5, q 0.002, down in 7 of 20 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[VAT1L]] (+0.67, fdr 2e-05), [[NHSL2]] (+0.66, fdr 7e-06), [[STXBP5L]] (+0.64, fdr 1e-05); moves opposite to [[SLC15A5]] (-0.47, fdr 3e-04).
> It is in [[Module 061]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[LYPD6B]] → it (grade B ⚠); 2 go from it, the strongest it → [[SYT7]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 33 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8147.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **3.49×** | +16.0 | 0e+00 | 15/20 (NCI-H460, NCI-H1573, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.15×** | +14.6 | 0e+00 | 6/17 (A549, C-33 A, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.92×** | +11.9 | 3e-30 | 4/7 (RPMI-7951, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.89×** | +9.6 | 1e-19 | 5/11 (RPMI-7951, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.02×** | +9.0 | 3e-17 | 5/16 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.62×** | +8.7 | 4e-16 | 14/19 (NCI-H460, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.40×** | +7.9 | 2e-13 | 16/21 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.33×** | +7.1 | 1e-10 | 4/7 (RPMI-7951, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift; position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **2.01×** | +6.3 | 2e-08 | 12/20 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.00×** | +6.3 | 2e-08 | 15/20 (NCI-H460, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.94×** | +5.9 | 1e-07 | 13/20 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.84×** | +5.5 | 2e-06 | 3/14 (NCI-H460, HOP62, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.82×** | +5.4 | 3e-06 | 6/17 (NCI-H460, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.52×** | +5.3 | 4e-06 | 4/20 (H4, NCI-H460, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.76×** | +5.1 | 2e-05 | 5/20 (C32, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.71×** | +4.8 | 5e-05 | 5/15 (A-427, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.70×** | +4.8 | 5e-05 | 5/20 (NCI-H460, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.67×** | +4.6 | 1e-04 | 5/17 (NCI-H460, HOP62, …) | top dose only |  |
| [[Rapamycin (drug)]] 0.5 µM |  | **1.48×** | +3.5 | 0.011 | 1/19 (A-172) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8147.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.870× | -4.6 | 0.002 | 4/21 (HOP62, NCI-H2030, …) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.609×** | -4.5 | 0.002 | 7/20 (HOP62, H4, …) | two highest doses |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | **0.636×** | -4.1 | 0.007 | 2/20 (NCI-H1573, BT-474) | two highest doses | position effect removed |
| [[Dexamethasone (drug)]] 5 µM |  | **0.683×** | -3.5 | 0.071 | 7/20 (H4, HOP62, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8147. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 7.69 | 6 (3 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 6.59× (z +11.2) | — |
| [[A-172 (line)]] | wt | 4.84 | 1 | 1 | [[Tucidinostat (drug)]] 5 µM 6.31× (z +9.4) | [[Bisoprolol (hemifumarate) (drug)]] 5 µM 0.0584× (z -9.8) |
| [[NCI-H1573 (line)]] | alt | 3.87 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 7.88× (z +9.9) | — |
| [[A-427 (line)]] | wt | 2.52 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 17.4× (z +9.9) | — |
| [[C32 (line)]] | wt | 6.94 | 0 | 1 | — | [[Trametinib (drug)]] 0.5 µM 0.125× (z -8.9) |
| [[HOP62 (line)]] | alt | 3.94 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.5 µM 0.0599× (z -8.9) |
| [[NCI-H2030 (line)]] | alt | 1.80 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 14.1× (z +8.7) | — |
| [[SNU-423 (line)]] | alt | 11.2 | 0 | 1 | — | [[Budesonide (drug)]] 0.5 µM 0.0652× (z -10.0) |
| [[A498 (line)]] | wt | 0.675 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.26 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.704 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 40.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.664 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.33 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.720 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.835 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.742 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.936 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.719 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.29 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.932 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.967 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.10 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.694 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.719 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.957 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.678 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.599 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.761 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.57 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.615 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 7.25 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.618 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.720 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.703 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.742 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.06 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.737 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 51.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.08 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.834 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.836 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.674 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8147), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VAT1L]] | +0.67 | +0.48 / +0.77 | both halves | 2e-05 |  |
| [[NHSL2]] | +0.66 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[STXBP5L]] | +0.64 | +0.53 / +0.57 | both halves | 1e-05 | **novel candidate** |
| [[SH3GL2]] | +0.64 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[PKNOX2]] | +0.61 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[KCNN3]] | +0.60 | +0.44 / +0.59 | both halves | 3e-05 |  |
| [[HS6ST3]] | +0.59 | +0.53 / +0.63 | both halves | 1e-05 |  |
| [[ALK]] | +0.59 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[EPHB1]] | +0.59 | +0.55 / +0.67 | both halves | 1e-05 |  |
| [[LINC02220]] | +0.59 | +0.48 / +0.61 | both halves | 2e-05 |  |
| [[DACH2]] | +0.59 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[ANOS1]] | +0.58 | +0.40 / +0.71 | both halves | 4e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC15A5]] | -0.47 | -0.57 / -0.26 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 1, C 7.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LYPD6B]] | B | LYPD6B activity raises COLEC12's level | lines that do not express LYPD6B (23) vs lines expressing it (27) | 1.62× lower at baseline in the lines without LYPD6B | 0.067 | ⚠ within organs, on part of the lines; also absent: GPR35, ATP2C2, EPHB6 |
| [[NHSL2]] | C | NHSL2 activity raises COLEC12's level | lines that do not express NHSL2 (24) vs lines expressing it (26) | 2.87× lower at baseline in the lines without NHSL2 | 0.025 | ⚠ within organs, on part of the lines; also absent: S1PR3, TWIST2, FBXL7; maybe low, not absent; co-absent with the target |
| [[SNAP91]] | C | SNAP91 activity raises COLEC12's level | lines that do not express SNAP91 (26) vs lines expressing it (24) | 2.99× lower at baseline in the lines without SNAP91 | 0.050 | ⚠ within organs, on part of the lines; also absent: CHST8, PLEKHG4B, COLEC12; maybe low, not absent; co-absent with the target |
| [[VIPR2]] | C | VIPR2 activity raises COLEC12's level | lines that do not express VIPR2 (32) vs lines expressing it (18) | 2.12× lower at baseline in the lines without VIPR2 | 0.057 | ⚠ within organs, on part of the lines; also absent: DPP10, KCNH5, ASXL3; maybe low, not absent; co-absent with the target |
| [[CHST8]] | C | CHST8 activity raises COLEC12's level | lines that do not express CHST8 (29) vs lines expressing it (21) | 2.62× lower at baseline in the lines without CHST8 | 0.057 | ⚠ within organs, on part of the lines; also absent: PLEKHG4B, JAKMIP1, SNAP91; co-absent with the target |
| [[SYNJ2]] | C | SYNJ2 activity lowers COLEC12's level | lines that do not express SYNJ2 (4) vs lines expressing it (46) | 1.59× higher at baseline in the lines without SYNJ2 | 0.086 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ZNF827, LINC01277, ITGA2-AS1; maybe low, not absent |
| [[PTPRN]] | C | PTPRN activity raises COLEC12's level | lines that do not express PTPRN (31) vs lines expressing it (19) | 2.79× lower at baseline in the lines without PTPRN | 0.088 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: SPARC, PAX3, PHACTR1; co-absent with the target |
| [[CLSTN2]] | C | CLSTN2 activity raises COLEC12's level | lines that do not express CLSTN2 (30) vs lines expressing it (20) | 2.95× lower at baseline in the lines without CLSTN2 | 0.098 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: TENM2, CCDC144NL-AS1, ENSG00000264660; co-absent with the target |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SYT7]] | B | COLEC12 activity lowers SYT7's level | lines that do not express COLEC12 (25) vs lines expressing it (25) | 1.31× higher at baseline in the lines without COLEC12 | 0.039 | ⚠ within organs, on part of the lines; also absent: GDNF-AS1, PIEZO2, SLC22A17; maybe low, not absent |
| [[NHSL2]] | C | COLEC12 activity raises NHSL2's level | lines that do not express COLEC12 (25) vs lines expressing it (25) | 1.97× lower at baseline in the lines without COLEC12 | 0.063 | ⚠ within organs, on part of the lines; also absent: GDNF-AS1, PIEZO2, SLC22A17; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 061]] — Neuronal System; 78 genes; every member is in the + arm (projection on the module's main direction 0.721). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (26.2, 32.9); signed map (32.6, 25.4). **Vector** length 49.1, 11.4% of its response variance represented; |z| ≥ 3 in 521 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.2 | +16.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.1 | +11.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.0 | +9.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.9 | +8.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.5 | +7.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.7 | +4.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.7 | +5.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.5 | +2.3 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.4 | +1.9 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.0 | -4.6 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.8 | -2.2 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.6 | -1.8 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -1.5 | -4.5 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.5 | -1.8 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -1.5 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | collectin subfamily member 12 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18p11.32 — chr18:316,737-500,722 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SRCL, CL-P1, SCARA4 |
| Gene groups (HGNC) | Collectins; Scavenger receptors; C-type lectin domain containing |
| Reactome | 5 pathways, smallest: Scavenging by Class A Receptors; Binding and Uptake of Ligands by Scavenger Receptors; Immunoregulatory interactions between a Lymphoid and a non-Lymphoid cell |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5KU26](https://www.uniprot.org/uniprotkb/Q5KU26) (Collectin-12):

> Scavenger receptor that displays several functions associated with host defense. Promotes binding and phagocytosis of Gram-positive, Gram-negative bacteria and yeast. Mediates the recognition, internalization and degradation of oxidatively modified low density lipoprotein (oxLDL) by vascular endothelial cells. Binds to several carbohydrates including Gal-type ligands, D-galactose, L- and D-fucose, GalNAc, T and Tn antigens in a calcium-dependent manner and internalizes specifically GalNAc in …

**Summary**, from NCBI Gene [81035](https://www.ncbi.nlm.nih.gov/gene/81035):

> This gene encodes a member of the C-lectin family, proteins that possess collagen-like sequences and carbohydrate recognition domains. This protein is a scavenger receptor that displays several functions associated with host defense. It can bind to carbohydrate antigens on microorganisms, facilitating their recognition and removal. It also mediates the recognition, internalization, and degradation of oxidatively modified low density lipoprotein by vascular endothelial cells. [provided by …

**Accessions** — [HGNC:16016](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16016) · Entrez [81035](https://www.ncbi.nlm.nih.gov/gene/81035) · UniProt [Q5KU26](https://www.uniprot.org/uniprotkb/Q5KU26) · Ensembl [ENSG00000158270](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000158270)

## Data

Gene col 8147: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8147); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8147, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8147]; `tensor/DDL_lfc|DDL_z.npy` [8147]; `embed/gene_vectors.npy` [8147]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8147 or target_col == 8147). Every well: [[COLEC12 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/COLEC12.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
