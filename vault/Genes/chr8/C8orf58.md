---
symbol: "C8orf58"
type: "gene"
col: 14289
ensembl_id: "ENSG00000241852"
name: "chromosome 8 open reading frame 58"
location: "8p21.3"
module: 218
arm: "+"
pooled_cpm: 7.0
n_lines_expressing: 47
n_dd_up: 0
n_dd_down: 37
n_dd_up_clean: 0
n_dd_down_clean: 28
in_vector_space: true
direction_upstream: 4
direction_downstream: 1
tags: ["gene", "module/218"]
generated_by: "tahoemap"
---

# C8orf58

*chromosome 8 open reading frame 58* — 8p21.3

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 37 drug-doses (9 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.284× (z -14.9, q 0e+00, down in 36 of 43 measured lines).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SYDE1]] (+0.54, fdr 1e-05), [[EFEMP2]] (+0.53, fdr 1e-04), [[MAPK7]] (+0.51, fdr 1e-05); moves opposite to [[SEL1L3]] (-0.54, fdr 3e-05), [[RUFY3]] (-0.50, fdr 3e-04), [[MYO5C]] (-0.49, fdr 4e-05).
> It is in [[Module 218]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → [[ZNF324]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14289.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Carbamazepine (drug)]] 5 µM |  | 1.35× | +3.6 | 0.18 | 5/42 (NCI-H2030, PANC-1, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | 1.32× | +3.3 | 0.24 | 2/45 (AsPC-1, A549) | inconsistent across doses |  |
| [[Roxadustat (drug)]] 5 µM |  | 1.32× | +3.2 | 0.24 | 4/42 (COLO 205, hTERT-HPNE, …) | top dose only | position effect removed |
| [[AZD2858 (drug)]] 5 µM | ⚠ toxic | 1.65× | +3.1 | 0.24 | 4/32 (MIA PaCa-2, Hs 766T, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 9 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 37 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14289.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.284×** | -14.9 | 0e+00 | 36/43 (LOX-IMVI, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.485×** | -12.1 | 2e-31 | 31/38 (MIA PaCa-2, HOP62, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.366×** | -11.9 | 2e-30 | 34/43 (HS-578T, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.368×** | -11.8 | 3e-30 | 33/43 (NCI-H1792, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.375×** | -11.6 | 3e-29 | 37/43 (HS-578T, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.376×** | -11.6 | 4e-29 | 36/42 (SW480, LS 180, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.368×** | -11.4 | 3e-28 | 34/42 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.523×** | -10.9 | 1e-25 | 27/41 (Hs 766T, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.404×** | -10.2 | 2e-22 | 32/42 (PANC-1, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.449×** | -9.1 | 4e-18 | 24/35 (Hs 766T, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.487×** | -8.5 | 7e-16 | 26/38 (RPMI-7951, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.499×** | -8.2 | 8e-15 | 26/44 (AsPC-1, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **0.513×** | -7.9 | 1e-13 | 19/25 (Hs 766T, LOX-IMVI, …) | inconsistent across doses | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.534×** | -7.4 | 4e-12 | 28/42 (LOX-IMVI, hTERT-HPNE, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.524×** | -7.4 | 6e-12 | 24/38 (SK-MEL-2, A-427, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.543×** | -7.2 | 1e-11 | 27/42 (NCI-H1573, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.556×** | -7.0 | 1e-10 | 22/42 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.42 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14289. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 12.3 | 0 | 9 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0641× (z -14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.161× (z -13.6) |
| [[Hs 766T (line)]] | wt | 23.9 | 0 | 8 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0305× (z -19.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.140× (z -15.5) |
| [[HS-578T (line)]] | alt | 14.6 | 0 | 8 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0921× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.119× (z -10.8) |
| [[NCI-H460 (line)]] | wt | 5.77 | 0 | 6 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.117× (z -11.7) |
| [[hTERT-HPNE (line)]] | wt | 13.0 | 0 | 5 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0712× (z -10.3) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.0768× (z -10.0) |
| [[SK-MEL-2 (line)]] | alt | 12.8 | 0 | 5 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.106× (z -10.2) |
| [[A-172 (line)]] | wt | 13.3 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.104× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.146× (z -10.2) |
| [[MIA PaCa-2 (line)]] | alt | 19.2 | 0 | 4 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.110× (z -11.6) ⚠ toxic; cell-cycle shift, explains ~34% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.263× (z -10.4) |
| [[RPMI-7951 (line)]] | alt | 11.8 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.0879× (z -13.7) |
| [[NCI-H2030 (line)]] | alt | 6.14 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.112× (z -9.5) ⚠ toxic · without an alert: [[Silodosin (drug)]] 5 µM 0.114× (z -9.4) |
| [[C32 (line)]] | wt | 8.49 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.208× (z -9.0) |
| [[CFPAC-1 (line)]] | alt | 5.99 | 0 | 1 | — | [[Bortezomib (drug)]] 0.05 µM 0.122× (z -8.9) |
| [[HOP62 (line)]] | alt | 5.84 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.190× (z -9.9) |
| [[KATO III (line)]] | alt | 5.71 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0687× (z -10.4) |
| [[LS 180 (line)]] | wt | 5.15 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0327× (z -12.0) |
| [[NCI-H1792 (line)]] | alt | 9.25 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.104× (z -10.3) |
| [[Panc 03.27 (line)]] | alt | 5.61 | 0 | 1 (1 ⚠) | — | [[Nimesulide (drug)]] 5 µM 0.0644× (z -9.6) ⚠ toxic; unreliable plate only |
| [[PANC-1 (line)]] | alt | 4.31 | 0 | 1 | — | [[Bortezomib (drug)]] 0.05 µM 0.101× (z -10.5) |
| [[SW480 (line)]] | alt | 5.08 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.108× (z -12.1) |
| [[A-427 (line)]] | wt | 6.44 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.64 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.70 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.12 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.80 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.63 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.00 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.80 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.57 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 4.08 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.37 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.27 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.38 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.59 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.56 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.15 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.67 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.48 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.24 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 9.63 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.71 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.57 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.68 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14289), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 4 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SYDE1]] | +0.54 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[EFEMP2]] | +0.53 | +0.60 / +0.35 | both halves | 1e-04 |  |
| [[MAPK7]] | +0.51 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[INAFM2]] | +0.51 | +0.45 / +0.52 | both halves | 3e-05 |  |
| [[EHD2]] | +0.49 | +0.55 / +0.40 | both halves | 5e-05 |  |
| [[RIN1]] | +0.49 | +0.48 / +0.44 | both halves | 3e-05 |  |
| [[PIM2]] | +0.48 | +0.34 / +0.46 | both halves | 1e-04 |  |
| [[LINC01615]] | +0.48 | +0.54 / +0.43 | both halves | 3e-05 |  |
| [[ARF6]] | +0.48 | +0.51 / +0.45 | both halves | 3e-05 |  |
| [[MRNIP]] | +0.48 | +0.42 / +0.32 | both halves | 2e-04 |  |
| [[ZNF574]] | +0.47 | +0.38 / +0.43 | both halves | 7e-05 |  |
| [[RARA]] | +0.47 | +0.53 / +0.37 | both halves | 8e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SEL1L3]] | -0.54 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[RUFY3]] | -0.50 | -0.56 / -0.27 | both halves | 3e-04 |  |
| [[MYO5C]] | -0.49 | -0.50 / -0.40 | both halves | 4e-05 |  |
| [[ACTR3C]] | -0.47 | -0.53 / -0.18 | ⚠ one half (not replicated) | 1e-03 |  |
| [[TRMT2B]] | -0.46 | -0.36 / -0.31 | both halves | 2e-04 |  |
| [[PAWR]] | -0.44 | -0.37 / -0.44 | both halves | 8e-05 |  |
| [[TOM1L1]] | -0.44 | -0.35 / -0.51 | both halves | 1e-04 |  |
| [[NSMAF]] | -0.44 | -0.50 / -0.29 | both halves | 2e-04 |  |
| [[PATJ]] | -0.43 | -0.47 / -0.34 | both halves | 1e-04 |  |
| [[UBE2K]] | -0.43 | -0.31 / -0.40 | both halves | 2e-04 |  |
| [[FAM149A]] | -0.43 | -0.37 / -0.34 | both halves | 1e-04 |  |
| [[TXN]] | -0.42 | -0.32 / -0.22 | both halves | 6e-04 |  |
| [[IDE]] | -0.42 | -0.43 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises C8orf58's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.4% of all compounds | 0.053 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ACTR3C]] | B | ACTR3C activity lowers C8orf58's level | lines that do not express ACTR3C (15) vs lines expressing it (35) | 1.79× higher at baseline in the lines without ACTR3C | 0.061 | ⚠ within organs, on part of the lines; also absent: LRRC61, ENPP4, ENSG00000263325 |
| [[SYDE1]] | B | SYDE1 activity raises C8orf58's level | lines that do not express SYDE1 (11) vs lines expressing it (39) | 1.61× lower at baseline in the lines without SYDE1 | 0.062 | ⚠ within organs, on part of the lines; co-occurs with APC, ACVR2A; also absent: DNAAF9, ZNF134, ENSG00000286964 |
| [[FSCN1]] | C | FSCN1 activity raises C8orf58's level | lines that do not express FSCN1 (4) vs lines expressing it (46) | 1.58× lower at baseline in the lines without FSCN1 | 0.076 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TXNRD3, ELK3, WWTR1; its own permutation p |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF324]] | C | C8orf58 activity lowers ZNF324's level | lines that do not express C8orf58 (3) vs lines expressing it (47) | 1.49× higher at baseline in the lines without C8orf58 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: HOMER3, APOBEC3F, TXNRD3; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 218]]; 12 genes; every member is in the + arm (projection on the module's main direction 0.396). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-10.8, 48.6); signed map (-30.3, 31.8). **Vector** length 60.9, 9.58% of its response variance represented; |z| ≥ 3 in 1,117 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +2.6 | +0.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.3 | -0.9 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +2.3 | +1.9 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | +2.1 | +1.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +1.5 | -11.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.5 | +3.3 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.4 | +2.6 |
|  | [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM |  | +1.1 | +2.1 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.1 | +2.6 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -4.2 | -11.8 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -4.0 | -10.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.0 | -11.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | -3.0 | -7.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -2.1 | -0.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.0 | -2.7 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.8 | -3.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.7 | -7.4 |
|  | [[Benztropine (mesylate) (drug)]] 0.05 µM |  | -1.4 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | chromosome 8 open reading frame 58 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p21.3 — chr8:22,599,599-22,604,150 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ34715 |
| Matched by | ensembl_id |

UniProt [Q8NAV2](https://www.uniprot.org/uniprotkb/Q8NAV2) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:32233](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:32233) · Entrez [541565](https://www.ncbi.nlm.nih.gov/gene/541565) · UniProt [Q8NAV2](https://www.uniprot.org/uniprotkb/Q8NAV2) · Ensembl [ENSG00000241852](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000241852)

## Data

Gene col 14289: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14289); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14289, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14289]; `tensor/DDL_lfc|DDL_z.npy` [14289]; `embed/gene_vectors.npy` [14289]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14289 or target_col == 14289). Every well: [[C8orf58 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/C8orf58.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
