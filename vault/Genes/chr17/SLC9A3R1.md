---
symbol: "SLC9A3R1"
type: "gene"
col: 3019
ensembl_id: "ENSG00000109062"
name: "NHERF family PDZ scaffold protein 1"
location: "17q25.1"
module: 162
arm: "+"
pooled_cpm: 26.06
n_lines_expressing: 49
n_dd_up: 21
n_dd_down: 0
n_dd_up_clean: 15
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/162"]
generated_by: "tahoemap"
---

# SLC9A3R1

*NHERF family PDZ scaffold protein 1* — 17q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 4.31× (z +19.8, q 0e+00, up in 45 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 1 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (HS-578T 0.0976×); [[Pitavastatin (Calcium) (drug)]] 0.05 µM in 1 line (SNU-1 0.0647×); [[Baicalin (drug)]] 0.5 µM in 1 line (RPMI-7951 0.0628×).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PLEKHO2]] (+0.63, fdr 1e-05), [[MADD]] (+0.61, fdr 1e-05), [[PNPLA2]] (+0.57, fdr 2e-05); moves opposite to [[RNPC3]] (-0.58, fdr 1e-04), [[WASH2P-1]] (-0.55, fdr 1e-04), [[COA6]] (-0.55, fdr 4e-05).
> It is in [[Module 162]], a single-armed module (estrogen response late).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[C1orf226]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3019.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **4.31×** | +19.8 | 0e+00 | 45/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.79×** | +18.1 | 0e+00 | 44/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **3.49×** | +17.0 | 0e+00 | 45/47 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.05×** | +13.8 | 4e-41 | 34/45 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.90×** | +8.7 | 4e-16 | 35/47 (SNU-423, A-172, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **1.91×** | +8.4 | 3e-15 | 21/26 (NCI-H460, HepG2/C3A, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.84×** | +8.3 | 9e-15 | 33/44 (A-172, PANC-1, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.67×** | +7.0 | 2e-10 | 33/47 (PANC-1, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **1.65×** | +6.8 | 7e-10 | 21/38 (A498, HepG2/C3A, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.61×** | +6.2 | 3e-08 | 25/46 (NCI-H1792, SW1417, …) | rises with dose | cell-cycle shift (explains ~20% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.58×** | +6.2 | 3e-08 | 25/45 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.38×** | +6.1 | 4e-08 | 27/47 (SK-MEL-2, HEC-1-A, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **2.07×** | +5.2 | 1e-05 | 22/47 (PANC-1, SNU-423, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.47×** | +5.0 | 2e-05 | 19/41 (HEC-1-A, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.87×** | +4.4 | 3e-04 | 18/43 (NCI-H23, J82, …) | top dose only | noisy plate (z scaled) |
| [[Cepharanthine (drug)]] 5 µM |  | **1.25×** | +4.2 | 9e-04 | 17/47 (HOP62, J82, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.27×** | +3.3 | 0.033 | 17/47 (HOP62, Panc 03.27, …) | top dose only |  |
| [[Aliskiren (drug)]] 0.5 µM |  | **1.26×** | +3.2 | 0.047 | 13/47 (LoVo, HT-29, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3019.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 1 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (HS-578T 0.0976×); [[Pitavastatin (Calcium) (drug)]] 0.05 µM in 1 line (SNU-1 0.0647×); [[Baicalin (drug)]] 0.5 µM in 1 line (RPMI-7951 0.0628×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Temsirolimus (drug)]] 0.5 µM |  | 0.769× | -3.6 | 0.15 | 17/42 (NCI-H2030, C32, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | 0.618× | -3.4 | 0.15 | 13/47 (A-427, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Saquinavir (drug)]] 5 µM |  | 0.842× | -3.3 | 0.15 | 17/45 (SHP-77, HCT15, …) | rises with dose | position effect removed |
| [[Carbamazepine (drug)]] 0.5 µM |  | 0.786× | -3.3 | 0.15 | 16/46 (SW 1271, NCI-H2347, …) | inconsistent across doses |  |
| [[Phenylephrine (hydrochloride) (drug)]] 0.5 µM |  | 0.801× | -3.0 | 0.27 | 6/47 (J82, HOP62, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3019. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 10.1 | 8 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 9.57× (z +14.2) | — |
| [[SW480 (line)]] | alt | 23.1 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 5.42× (z +14.8) | — |
| [[A549 (line)]] | wt | 11.9 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 11.6× (z +12.5) | — |
| [[J82 (line)]] | alt | 13.5 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 7.65× (z +12.5) | — |
| [[SNU-423 (line)]] | alt | 22.3 | 4 | 0 | [[Auranofin (drug)]] 5 µM 9.27× (z +14.4) | — |
| [[A-427 (line)]] | wt | 21.0 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.19× (z +10.3) | — |
| [[HOP62 (line)]] | alt | 8.99 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.05× (z +12.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 12.8 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 8.53× (z +11.1) | — |
| [[NCI-H2030 (line)]] | alt | 13.1 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 5.66× (z +10.0) | — |
| [[Panc 03.27 (line)]] | alt | 17.1 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 6.56× (z +11.0) | — |
| [[PANC-1 (line)]] | alt | 18.7 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 7.06× (z +15.9) | — |
| [[SK-MEL-2 (line)]] | alt | 15.8 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 6.68× (z +10.5) | — |
| [[HEC-1-A (line)]] | alt | 14.6 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 4.46× (z +10.2) | — |
| [[HS-578T (line)]] | alt | 8.21 | 1 | 1 | [[Panobinostat (drug)]] 5 µM 6.74× (z +8.9) | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.0976× (z -10.8) |
| [[RPMI-7951 (line)]] | alt | 6.86 | 0 | 2 (1 ⚠) | — | [[Baicalin (drug)]] 0.5 µM 0.0628× (z -9.6) |
| [[SNU-1 (line)]] | wt | 13.8 | 0 | 2 | — | [[Pitavastatin (Calcium) (drug)]] 0.05 µM 0.0647× (z -10.2) |
| [[SW1417 (line)]] | alt | 60.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +10.0) | — |
| [[A-172 (line)]] | wt | 44.1 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.93× (z +11.5) | — |
| [[AsPC-1 (line)]] | alt | 14.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.06× (z +11.3) | — |
| [[C32 (line)]] | wt | 7.85 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.54× (z +8.9) | — |
| [[CFPAC-1 (line)]] | alt | 13.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.43× (z +11.9) | — |
| [[COLO 205 (line)]] | alt | 31.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.41× (z +10.0) | — |
| [[H4 (line)]] | wt | 7.54 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 16.7× (z +8.6) | — |
| [[LoVo (line)]] | wt | 23.0 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.83× (z +10.0) | — |
| [[NCI-H1792 (line)]] | alt | 9.34 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 7.70× (z +8.9) | — |
| [[NCI-H2347 (line)]] | alt | 14.4 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.63× (z +8.7) | — |
| [[RKO (line)]] | wt | 25.1 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.07× (z +8.6) | — |
| [[SW 900 (line)]] | alt | 18.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.60× (z +10.0) | — |
| [[SW48 (line)]] | wt | 19.9 | 0 | 1 | — | [[Orlistat (drug)]] 0.05 µM 0.112× (z -9.4) |
| [[A498 (line)]] | wt | 131 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 45.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.93 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 32.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 79.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.22 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 83.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.34 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 43.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3019), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*56 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLEKHO2]] | +0.63 | +0.59 / +0.57 | both halves | 1e-05 |  |
| [[MADD]] | +0.61 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[PNPLA2]] | +0.57 | +0.66 / +0.47 | both halves | 2e-05 |  |
| [[UBA1]] | +0.57 | +0.63 / +0.47 | both halves | 2e-05 |  |
| [[PITPNM1]] | +0.56 | +0.41 / +0.45 | both halves | 4e-05 |  |
| [[NR4A1]] | +0.55 | +0.46 / +0.49 | both halves | 2e-05 |  |
| [[RALY]] | +0.55 | +0.40 / +0.44 | both halves | 5e-05 | same gene group |
| [[EPHB3]] | +0.55 | +0.43 / +0.49 | both halves | 3e-05 |  |
| [[UBE2S]] | +0.55 | +0.42 / +0.48 | both halves | 4e-05 |  |
| [[NCKAP5L]] | +0.54 | +0.51 / +0.44 | both halves | 3e-05 |  |
| [[STARD5]] | +0.53 | +0.44 / +0.49 | both halves | 3e-05 |  |
| [[LRCH4]] | +0.53 | +0.54 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*44 of its nearest partners move opposite, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNPC3]] | -0.58 | -0.54 / -0.35 | both halves | 1e-04 |  |
| [[WASH2P-1]] | -0.55 | -0.35 / -0.50 | both halves | 1e-04 |  |
| [[COA6]] | -0.55 | -0.44 / -0.41 | both halves | 4e-05 |  |
| [[ANGEL2]] | -0.53 | -0.43 / -0.42 | both halves | 4e-05 |  |
| [[TRAPPC13]] | -0.53 | -0.39 / -0.41 | both halves | 6e-05 |  |
| [[C2orf42]] | -0.52 | -0.40 / -0.40 | both halves | 5e-05 |  |
| [[GPALPP1]] | -0.52 | -0.43 / -0.37 | both halves | 7e-05 |  |
| [[VPS13B-DT]] | -0.51 | -0.43 / -0.34 | both halves | 1e-04 |  |
| [[FAM185A]] | -0.51 | -0.39 / -0.37 | both halves | 9e-05 |  |
| [[INTS9]] | -0.50 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[GTPBP10]] | -0.50 | -0.49 / -0.35 | both halves | 1e-04 |  |
| [[SDHAF4]] | -0.49 | -0.44 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C1orf226]] | B | C1orf226 activity raises SLC9A3R1's level | lines that do not express C1orf226 (14) vs lines expressing it (36) | 2.02× lower at baseline in the lines without C1orf226 | 0.032 | ⚠ within organs, on part of the lines; also absent: ENSG00000254706, EPS8L2, EEPD1; maybe low, not absent |
| [[EPPK1]] | B | EPPK1 activity raises SLC9A3R1's level | lines that do not express EPPK1 (25) vs lines expressing it (25) | 1.40× lower at baseline in the lines without EPPK1 | 0.081 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, EPCAM, CLDN3 |
| [[FZD5]] | C | FZD5 activity raises SLC9A3R1's level | lines that do not express FZD5 (4) vs lines expressing it (46) | 2.30× lower at baseline in the lines without FZD5 | 0.078 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: PCBD1, KIAA1671, TUFT1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 162]] — estrogen response late; 26 genes; every member is in the + arm (projection on the module's main direction 0.596). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.0, -6.6); signed map (-6.5, 20.8). **Vector** length 85.4, 17.9% of its response variance represented; |z| ≥ 3 in 1,076 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +3.8 | +13.8 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | +3.7 | +2.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.7 | +19.8 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.4 | +18.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.3 | +8.7 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.2 | +4.4 |
|  | [[Posaconazole (drug)]] 5 µM |  | +2.2 | +2.0 |
|  | [[(S)-Crizotinib (drug)]] 5 µM |  | +2.1 | +1.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.0 | +6.1 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -5.4 | -0.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -5.2 | +1.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.5 | +0.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.9 | -1.1 |
|  | [[TAK-901 (drug)]] 5 µM |  | -2.9 | -3.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.3 | -1.2 |
|  | [[Rapamycin (drug)]] 0.5 µM |  | -2.0 | -2.0 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | -1.9 | -3.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.9 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | NHERF family PDZ scaffold protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.1 — chr17:74,748,628-74,769,353 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NHERF, EBP50, NHERF-1, NHE-RF; previously SLC9A3R1 |
| Gene groups (HGNC) | PDZ domain containing; MicroRNA protein coding host genes; NHERF family PDZ scaffold proteins |
| Hallmark sets | ESTROGEN_RESPONSE_LATE, ESTROGEN_RESPONSE_EARLY, MTORC1_SIGNALING |
| Matched by | ensembl_id |

**Function**, from UniProt [O14745](https://www.uniprot.org/uniprotkb/O14745) (Na(+)/H(+) exchange regulatory cofactor NHE-RF1):

> Scaffold protein that connects plasma membrane proteins with members of the ezrin/moesin/radixin family and thereby helps to link them to the actin cytoskeleton and to regulate their surface expression. Necessary for recycling of internalized ADRB2. Was first known to play a role in the regulation of the activity and subcellular location of SLC9A3. Necessary for cAMP-mediated phosphorylation and inhibition of SLC9A3. May enhance Wnt signaling. May participate in HTR4 targeting to microvilli (By …

**Summary**, from NCBI Gene [9368](https://www.ncbi.nlm.nih.gov/gene/9368):

> This gene encodes a sodium/hydrogen exchanger regulatory cofactor. The protein interacts with and regulates various proteins including the cystic fibrosis transmembrane conductance regulator and G-protein coupled receptors such as the beta2-adrenergic receptor and the parathyroid hormone 1 receptor. The protein also interacts with proteins that function as linkers between integral membrane and cytoskeletal proteins. The protein localizes to actin-rich structures including membrane ruffles, …

**Accessions** — [HGNC:11075](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11075) · Entrez [9368](https://www.ncbi.nlm.nih.gov/gene/9368) · UniProt [O14745](https://www.uniprot.org/uniprotkb/O14745) · Ensembl [ENSG00000109062](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000109062)

## Data

Gene col 3019: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3019); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3019, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3019]; `tensor/DDL_lfc|DDL_z.npy` [3019]; `embed/gene_vectors.npy` [3019]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3019 or target_col == 3019). Every well: [[SLC9A3R1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC9A3R1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
