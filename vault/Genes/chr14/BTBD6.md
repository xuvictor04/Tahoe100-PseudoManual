---
symbol: "BTBD6"
type: "gene"
col: 11585
ensembl_id: "ENSG00000184887"
name: "BTB domain containing 6"
location: "14q32.33"
module: 24
arm: "+"
pooled_cpm: 3.09
n_lines_expressing: 42
n_dd_up: 5
n_dd_down: 11
n_dd_up_clean: 0
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 1
direction_downstream: 5
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# BTBD6

*BTB domain containing 6* — 14q32.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.18× (z +9.7, q 3e-19, up in 12 of 17 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.481× (z -7.0, q 2e-09, down in 20 of 30 measured lines).
> Its strongest partners by |cos| (73 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 29 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF524]] (+0.60, fdr 1e-04), [[JOSD2]] (+0.59, fdr 4e-04), [[TSR3]] (+0.59, fdr 2e-05); moves opposite to [[CTSC]] (-0.55, fdr 3e-05), [[PRKAR1A]] (-0.48, fdr 8e-04, ⚠ not reproduced), [[STK26]] (-0.48, fdr 2e-04), [[ELK4]] (-0.48, fdr 6e-04).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[NME3]] → it (grade B ⚠); 5 go from it, the strongest it → [[C18orf21]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 5 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11585.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.18×** | +9.7 | 3e-19 | 12/17 (HEC-1-A, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.56×** | +8.3 | 4e-14 | 4/4 (CFPAC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.04×** | +4.5 | 0.002 | 5/8 (HEC-1-A, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.83×** | +4.1 | 0.006 | 7/15 (LS 180, KATO III, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~11% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.74×** | +3.6 | 0.036 | 4/19 (KATO III, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, none with an alert. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11585.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.481×** | -7.0 | 2e-09 | 20/30 (HT-29, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.373×** | -6.6 | 9e-09 | 25/37 (NCI-H2030, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.440×** | -5.5 | 6e-06 | 23/35 (KATO III, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.590×** | -5.0 | 7e-05 | 16/29 (NCI-H2030, LoVo, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.551×** | -3.9 | 0.013 | 11/32 (NCI-H2347, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.571×** | -3.8 | 0.016 | 16/29 (NCI-H2347, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.589×** | -3.6 | 0.030 | 12/36 (HS-578T, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.600×** | -3.4 | 0.042 | 11/34 (NCI-H1792, AN3 CA, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.616×** | -3.3 | 0.071 | 14/33 (SNU-1, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.621×** | -3.2 | 0.076 | 15/37 (hTERT-HPNE, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Benproperine (phosphate) (drug)]] 0.05 µM |  | **0.603×** | -3.1 | 0.085 | 5/35 (LoVo, RPMI-7951, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | 0.634× | -3.1 | 0.10 | 12/35 (BT-474, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11585. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 3.46 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.105× (z -9.7) |
| [[KATO III (line)]] | alt | 6.00 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0415× (z -11.4) |
| [[LoVo (line)]] | wt | 3.89 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.176× (z -8.8) |
| [[NCI-H2030 (line)]] | alt | 9.76 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.124× (z -9.6) |
| [[A-172 (line)]] | wt | 0.208 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.191 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.80 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.55 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.23 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.250 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 4.18 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.91 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.92 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.32 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.97 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.16 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.69 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.18 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.226 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.91 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.72 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.92 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.86 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.98 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.170 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.32 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.03 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.28 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.183 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.168 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.04 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.02 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.272 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 3.54 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.50 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.96 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.40 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.62 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11585), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 28 of them with an alert (⚠; 26 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF524]] | +0.60 | +0.32 / +0.63 | both halves | 1e-04 |  |
| [[JOSD2]] | +0.59 | +0.26 / +0.65 | both halves | 4e-04 |  |
| [[TSR3]] | +0.59 | +0.48 / +0.60 | both halves | 2e-05 |  |
| [[ENKD1]] | +0.58 | +0.27 / +0.66 | both halves | 3e-04 |  |
| [[STX18]] | +0.57 | +0.32 / +0.43 | both halves | 2e-04 |  |
| [[SSNA1]] | +0.57 | +0.23 / +0.60 | both halves | 5e-04 |  |
| [[MRPL55]] | +0.56 | +0.35 / +0.55 | both halves | 1e-04 |  |
| [[UCK1]] | +0.55 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[THAP7]] | +0.54 | +0.35 / +0.47 | both halves | 1e-04 |  |
| [[CDK5]] | +0.54 | +0.33 / +0.54 | both halves | 1e-04 |  |
| [[SAC3D1]] | +0.54 | +0.17 / +0.61 | ⚠ one half (not replicated) | 0.001 |  |
| [[MRPL43]] | +0.54 | +0.28 / +0.53 | both halves | 3e-04 |  |
| [[MYG1]] | +0.53 | +0.36 / +0.49 | both halves | 9e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CTSC]] | -0.55 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[PRKAR1A]] | -0.48 | -0.20 / -0.48 | ⚠ not reproduced | 8e-04 |  |
| [[STK26]] | -0.48 | -0.32 / -0.50 | both halves | 2e-04 |  |
| [[ELK4]] | -0.48 | -0.22 / -0.47 | both halves | 6e-04 |  |
| [[IGF2BP3]] | -0.48 | -0.42 / -0.29 | both halves | 2e-04 |  |
| [[SLC39A10]] | -0.46 | -0.30 / -0.40 | both halves | 2e-04 |  |
| [[TMEM123]] | -0.45 | -0.20 / -0.50 | both halves | 7e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NME3]] | B | NME3 activity raises BTBD6's level | lines that do not express NME3 (5) vs lines expressing it (45) | 2.80× lower at baseline in the lines without NME3 | 0.060 | ⚠ within organs, on part of the lines; also absent: TACC2; its own permutation p |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C18orf21]] | B | BTBD6 activity lowers C18orf21's level | lines that do not express BTBD6 (8) vs lines expressing it (42) | 1.25× higher at baseline in the lines without BTBD6 | 0.075 | ⚠ within organs, on part of the lines; also absent: ENSG00000225647, ENSG00000254394, RPL23AP49 |
| [[PACSIN3]] | B | BTBD6 activity lowers PACSIN3's level | lines that do not express BTBD6 (8) vs lines expressing it (42) | 1.40× higher at baseline in the lines without BTBD6 | 0.077 | ⚠ within organs, on part of the lines; also absent: ENSG00000225647, ENSG00000254394, RPL23AP49 |
| [[NME3]] | B | BTBD6 activity raises NME3's level | lines that do not express BTBD6 (8) vs lines expressing it (42) | 1.76× lower at baseline in the lines without BTBD6 | 0.083 | ⚠ within organs, on part of the lines; also absent: ENSG00000225647, ENSG00000254394, RPL23AP49 |
| [[COX14]] | B | BTBD6 activity lowers COX14's level | lines that do not express BTBD6 (8) vs lines expressing it (42) | 1.08× higher at baseline in the lines without BTBD6 | 0.089 | ⚠ within organs, on part of the lines; also absent: ENSG00000225647, ENSG00000254394, RPL23AP49 |
| [[MIIP]] | B | BTBD6 activity lowers MIIP's level | lines that do not express BTBD6 (8) vs lines expressing it (42) | 1.25× higher at baseline in the lines without BTBD6 | 0.096 | ⚠ within organs, on part of the lines; also absent: ENSG00000225647, ENSG00000254394, RPL23AP49 |

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.488). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-44.2, -15.0); signed map (-18.3, -4.9). **Vector** length 31.7, 3.58% of its response variance represented; |z| ≥ 3 in 593 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.2 | +2.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.1 | +8.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.9 | +9.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +1.9 | +3.6 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +1.6 | +4.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.4 | +1.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.2 | +1.2 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.0 | +1.4 |
|  | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | +1.0 | +2.2 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +1.0 | +1.4 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.2 | -5.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.8 | -6.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -1.3 | -3.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -1.3 | -3.1 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -1.1 | -3.3 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.1 | -1.6 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.0 | -2.5 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.0 | -2.0 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -0.9 | -2.2 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -0.9 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | BTB domain containing 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q32.33 — chr14:105,248,533-105,251,093 (+) |
| Ensembl biotype | protein_coding |
| Also known as | BDPL |
| Gene groups (HGNC) | BTB domain containing |
| Reactome | 4 pathways, smallest: Neddylation; Antigen processing: Ubiquitination & Proteasome degradation; Class I MHC mediated antigen processing & presentation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96KE9](https://www.uniprot.org/uniprotkb/Q96KE9) (BTB/POZ domain-containing protein 6):

> Adapter protein for the cul3 E3 ubiquitin-protein ligase complex (By similarity). Involved in late neuronal development and muscle formation (By similarity).

**Summary**, from NCBI Gene [90135](https://www.ncbi.nlm.nih.gov/gene/90135):

> Predicted to be involved in neurogenesis. Predicted to be located in cytoplasm. Predicted to be active in cytosol. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:19897](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19897) · Entrez [90135](https://www.ncbi.nlm.nih.gov/gene/90135) · UniProt [Q96KE9](https://www.uniprot.org/uniprotkb/Q96KE9) · Ensembl [ENSG00000184887](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000184887)

## Data

Gene col 11585: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11585); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11585, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11585]; `tensor/DDL_lfc|DDL_z.npy` [11585]; `embed/gene_vectors.npy` [11585]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11585 or target_col == 11585). Every well: [[BTBD6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BTBD6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
