---
symbol: "KBTBD12"
type: "gene"
col: 11938
ensembl_id: "ENSG00000187715"
name: "kelch repeat and BTB domain containing 12"
location: "3q21.3"
module: 55
arm: "+"
pooled_cpm: 2.34
n_lines_expressing: 16
n_dd_up: 23
n_dd_down: 1
n_dd_up_clean: 11
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 4
direction_downstream: 3
tags: ["gene", "module/055"]
generated_by: "tahoemap"
---

# KBTBD12

*kelch repeat and BTB domain containing 12* — 3q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (12 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.51× (z +15.7, q 0e+00, up in 7 of 8 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.5 µM: 0.547× (z -4.0, q 0.040, down in 2 of 12 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 6 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (KATO III 0.102×; ⚠ toxic); [[Dinaciclib (drug)]] 0.05 µM in 1 line (KATO III 0.119×; ⚠ toxic; transcription drop); [[Digitoxin (drug)]] 0.5 µM in 1 line (LS 180 0.106×; ⚠ cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC01956]] (+0.71, fdr 1e-05), [[CFTR]] (+0.63, fdr 4e-05), [[AP3B2]] (+0.61, fdr 8e-05); moves opposite to [[STRAP]] (-0.48, fdr 5e-05).
> It is in [[Module 055]], a single-armed module (Regulation of FZD by ubiquitination).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[FBXO15]] → it (grade B ⚠); 3 go from it, the strongest it → [[PHACTR2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 12 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11938.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.51×** | +15.7 | 0e+00 | 7/8 (HEC-1-A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **3.27×** | +10.9 | 3e-25 | 3/8 (NCI-H2347, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.90×** | +10.0 | 4e-21 | 1/3 (NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **3.95×** | +8.9 | 5e-17 | 2/7 (NCI-H2347, J82) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.78×** | +8.7 | 5e-16 | 1/4 (NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.64×** | +7.8 | 7e-13 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.91×** | +6.9 | 3e-10 | 4/8 (NCI-H2347, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.40×** | +5.7 | 9e-07 | 5/10 (HEC-1-A, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.76×** | +5.2 | 1e-05 | 3/12 (NCI-H2347, LS 180, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.16×** | +4.8 | 9e-05 | 0/3 | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.04×** | +4.6 | 2e-04 | 0/4 | top dose only | cell-cycle shift (explains ~2% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.02×** | +4.6 | 2e-04 | 0/3 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~3% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.63×** | +4.5 | 4e-04 | 4/13 (NCI-H2347, J82, …) | top dose only |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.94×** | +4.3 | 7e-04 | 0/5 | inconsistent across doses | low cells (technical?) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.94×** | +4.1 | 0.001 | 1/5 (NCI-H2347) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.86×** | +3.9 | 0.004 | 0/8 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.91×** | +3.0 | 0.072 | 0/4 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.58×** | +3.0 | 0.076 | 1/4 (KATO III) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11938.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 6 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (KATO III 0.102×; ⚠ toxic); [[Dinaciclib (drug)]] 0.05 µM in 1 line (KATO III 0.119×; ⚠ toxic; transcription drop); [[Digitoxin (drug)]] 0.5 µM in 1 line (LS 180 0.106×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.5 µM |  | **0.547×** | -4.0 | 0.040 | 2/12 (A549, SW 900) | inconsistent across doses |  |
| [[Pravastatin (sodium) (drug)]] 0.5 µM |  | 0.611× | -3.3 | 0.32 | 1/13 (SW 900) | inconsistent across doses |  |
| [[Artesunate (drug)]] 0.5 µM |  | 0.630× | -3.1 | 0.42 | 1/12 (Panc 03.27) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11938. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 29.2 | 0 | 5 (5 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.102× (z -11.6) ⚠ toxic |
| [[LS 180 (line)]] | wt | 17.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.106× (z -9.5) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 0.479 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.389 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.529 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.08 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.561 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.457 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.533 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.489 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.504 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.483 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.530 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.441 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.446 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.491 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.621 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.503 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.498 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.409 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.432 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.534 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.495 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.476 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.449 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.394 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.497 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.434 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.454 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.589 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.802 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.426 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.764 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.616 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.423 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.505 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.831 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.969 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.520 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.458 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.618 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.518 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.746 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.505 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.541 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.470 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11938), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01956]] | +0.71 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[CFTR]] | +0.63 | +0.68 / +0.42 | both halves | 4e-05 |  |
| [[AP3B2]] | +0.61 | +0.55 / +0.37 | both halves | 8e-05 |  |
| [[TNFSF15]] | +0.61 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[NEMP2-DT]] | +0.60 | +0.62 / +0.30 | both halves | 2e-04 |  |
| [[MUC12]] | +0.60 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[ZNF503-AS1]] | +0.60 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[NPSR1-AS1]] | +0.60 | +0.63 / +0.45 | both halves | 3e-05 |  |
| [[DENND2D]] | +0.59 | +0.58 / +0.33 | both halves | 1e-04 |  |
| [[SYK]] | +0.59 | +0.51 / +0.46 | both halves | 3e-05 |  |
| [[GNA14]] | +0.59 | +0.53 / +0.41 | both halves | 4e-05 |  |
| [[ABO]] | +0.58 | +0.47 / +0.51 | both halves | 2e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STRAP]] | -0.48 | -0.39 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 1, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FBXO15]] | B | FBXO15 activity lowers KBTBD12's level | lines that do not express FBXO15 (6) vs lines expressing it (44) | 2.08× higher at baseline in the lines without FBXO15 | 0.013 | ⚠ within organs, on part of the lines; also absent: DNAI1, EFCAB6, KCNK15-AS1 |
| [[LINC01956]] | C | LINC01956 activity raises KBTBD12's level | lines that do not express LINC01956 (38) vs lines expressing it (12) | 1.61× lower at baseline in the lines without LINC01956 | 0.017 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01440, SYT4, LINC03000; co-absent with the target |
| [[ST6GALNAC1]] | C | ST6GALNAC1 activity raises KBTBD12's level | lines that do not express ST6GALNAC1 (37) vs lines expressing it (13) | 1.96× lower at baseline in the lines without ST6GALNAC1 | 0.062 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC6A14, SLC44A4, STEAP4; co-absent with the target |
| [[TMEM30B]] | C | TMEM30B activity raises KBTBD12's level | lines that do not express TMEM30B (35) vs lines expressing it (15) | 1.80× lower at baseline in the lines without TMEM30B | 0.095 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, ANKRD22, RAB25; co-absent with the target |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 1, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PHACTR2]] | B | KBTBD12 activity lowers PHACTR2's level | lines that do not express KBTBD12 (34) vs lines expressing it (16) | 1.43× higher at baseline in the lines without KBTBD12 | 0.099 | ⚠ within organs, on part of the lines; also absent: GLP2R, SLC19A3, TSPYL5; maybe low, not absent |
| [[SULT1C2]] | C | KBTBD12 activity raises SULT1C2's level | lines that do not express KBTBD12 (34) vs lines expressing it (16) | 1.49× lower at baseline in the lines without KBTBD12 | 0.049 | ⚠ within organs, on part of the lines; also absent: GLP2R, SLC19A3, TSPYL5; maybe low, not absent; co-absent with the target |
| [[CFTR]] | C | KBTBD12 activity raises CFTR's level | lines that do not express KBTBD12 (34) vs lines expressing it (16) | 1.45× lower at baseline in the lines without KBTBD12 | 0.099 | ⚠ within organs, on part of the lines; also absent: GLP2R, SLC19A3, TSPYL5; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 055]] — Regulation of FZD by ubiquitination; 87 genes; every member is in the + arm (projection on the module's main direction 0.556). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (22.5, 49.1); signed map (63.5, 7.5). **Vector** length 22.7, 5.16% of its response variance represented; |z| ≥ 3 in 246 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.5 | +15.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.4 | +10.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.3 | +10.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.0 | +8.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.0 | +7.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.5 | +4.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.2 | +8.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +0.9 | +2.0 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +0.7 | +1.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +0.7 | +1.4 |
| fall | [[Artesunate (drug)]] 0.5 µM |  | -0.6 | -3.1 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -0.6 | -2.5 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.6 | -1.7 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -0.5 | -2.4 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -0.5 | -2.5 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -0.5 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | kelch repeat and BTB domain containing 12 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q21.3 — chr3:127,915,232-127,987,671 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ46299; previously KLHDC6 |
| Gene groups (HGNC) | BTB domain containing |
| Matched by | ensembl_id |

UniProt [Q3ZCT8](https://www.uniprot.org/uniprotkb/Q3ZCT8) carries no function annotation.

**Summary**, from NCBI Gene [166348](https://www.ncbi.nlm.nih.gov/gene/166348):

> Predicted to enable ubiquitin-like ligase-substrate adaptor activity. Predicted to be involved in proteasome-mediated ubiquitin-dependent protein catabolic process. Predicted to be part of Cul3-RING ubiquitin ligase complex. Predicted to be active in cytoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25731](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25731) · Entrez [166348](https://www.ncbi.nlm.nih.gov/gene/166348) · UniProt [Q3ZCT8](https://www.uniprot.org/uniprotkb/Q3ZCT8) · Ensembl [ENSG00000187715](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000187715)

## Data

Gene col 11938: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11938); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11938, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11938]; `tensor/DDL_lfc|DDL_z.npy` [11938]; `embed/gene_vectors.npy` [11938]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11938 or target_col == 11938). Every well: [[KBTBD12 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KBTBD12.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
