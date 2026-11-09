---
symbol: "MIR22HG"
type: "gene"
col: 11835
ensembl_id: "ENSG00000186594"
name: "MIR22 host gene"
location: "17p13.3"
module: 38
arm: "+"
pooled_cpm: 20.81
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 23
n_dd_up_clean: 11
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/038"]
generated_by: "tahoemap"
---

# MIR22HG

*MIR22 host gene* — 17p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (4 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 3.20× (z +12.7, q 3e-34, up in 46 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (5 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.678× (z -6.1, q 8e-07, down in 28 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C6orf62]] (+0.63, fdr 7e-06), [[FLACC1]] (+0.61, fdr 1e-05), [[TLCD2]] (+0.60, fdr 1e-05, ⚠ same locus), [[THUMPD3-AS1]] (+0.60, fdr 1e-05); moves opposite to [[KDM1A]] (-0.62, fdr 7e-06), [[SKP2]] (-0.62, fdr 7e-06), [[CTDSPL2]] (-0.61, fdr 1e-05).
> It is in [[Module 038]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[TMEM92-AS1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 4 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11835.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **3.20×** | +12.7 | 3e-34 | 46/47 (NCI-H2347, A-172, …) | top dose only | position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.22×** | +12.3 | 2e-32 | 36/47 (NCI-H1792, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.39×** | +9.5 | 3e-19 | 32/44 (A498, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.21×** | +7.4 | 3e-11 | 26/48 (SW480, SW 900, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.56×** | +6.9 | 8e-10 | 31/44 (MIA PaCa-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.53×** | +4.7 | 3e-04 | 15/36 (Panc 03.27, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.33×** | +4.4 | 1e-03 | 17/48 (A-172, NCI-H2030, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.47×** | +4.2 | 0.002 | 21/46 (LS 180, LoVo, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.49×** | +4.2 | 0.002 | 20/46 (RKO, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.51×** | +4.1 | 0.002 | 11/31 (SW480, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.38×** | +3.4 | 0.035 | 16/41 (CFPAC-1, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Vilanterol (drug)]] 5 µM |  | **1.22×** | +3.1 | 0.085 | 9/48 (A498, LS 180, …) | top dose only | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.33×** | +3.1 | 0.085 | 16/48 (LS 180, KATO III, …) | two highest doses |  |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.55×** | +3.1 | 0.085 | 12/47 (LS 180, Hs 766T, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.22×** | +3.1 | 0.085 | 15/48 (KATO III, PANC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11835.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **0.678×** | -6.1 | 8e-07 | 28/48 (AsPC-1, HS-578T, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.605×** | -5.5 | 9e-06 | 27/48 (KATO III, LoVo, …) | top dose only | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.597×** | -5.5 | 9e-06 | 24/43 (LoVo, COLO 205, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.712×** | -5.3 | 2e-05 | 32/48 (CFPAC-1, LoVo, …) | rises with dose | position effect removed |
| [[NG25 (drug)]] 5 µM |  | **0.418×** | -5.0 | 6e-05 | 27/46 (SHP-77, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **0.635×** | -5.0 | 6e-05 | 28/48 (LoVo, NCI-H2030, …) | top dose only | position effect removed |
| [[Selinexor (drug)]] 0.5 µM |  | **0.655×** | -4.7 | 3e-04 | 26/47 (AsPC-1, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Radotinib (drug)]] 5 µM |  | **0.745×** | -4.6 | 3e-04 | 23/48 (AsPC-1, CHP-212, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.659×** | -4.6 | 3e-04 | 25/48 (A498, SW 900, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.690×** | -4.1 | 0.003 | 23/48 (A498, HepG2/C3A, …) | all doses, flat | cell-cycle shift (explains ~14% here) |
| [[Ralimetinib dimesylate (drug)]] 5 µM |  | **0.533×** | -3.6 | 0.015 | 15/47 (COLO 205, Hs 766T, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.722×** | -3.6 | 0.016 | 20/48 (SW 1271, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Bentamapimod (drug)]] 5 µM |  | **0.558×** | -3.3 | 0.036 | 12/47 (HT-29, LOX-IMVI, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **0.564×** | -3.3 | 0.038 | 14/48 (AsPC-1, HT-29, …) | rises with dose | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **0.733×** | -3.3 | 0.038 | 19/45 (HepG2/C3A, hTERT-HPNE, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.584×** | -3.1 | 0.067 | 15/46 (BT-474, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.757×** | -3.1 | 0.067 | 14/47 (HS-578T, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~8% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.32 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11835. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 37.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.34× (z +14.2) | — |
| [[LoVo (line)]] | wt | 34.5 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.12× (z +15.1) | [[Niclosamide (olamine) (drug)]] 5 µM 0.228× (z -9.3) ⚠ toxic |
| [[NCI-H23 (line)]] | alt | 19.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.13× (z +14.9) | — |
| [[PANC-1 (line)]] | alt | 9.25 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.29× (z +9.0) | — |
| [[RPMI-7951 (line)]] | alt | 25.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.76× (z +11.4) | — |
| [[A-172 (line)]] | wt | 36.2 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.43× (z +9.0) | — |
| [[AsPC-1 (line)]] | alt | 41.6 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.296× (z -12.0) |
| [[C32 (line)]] | wt | 9.14 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.23× (z +9.1) | — |
| [[COLO 205 (line)]] | alt | 29.0 | 1 | 0 | [[Auranofin (drug)]] 5 µM 6.40× (z +8.6) | — |
| [[HepG2_C3A (line)]] | wt | 32.5 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.0635× (z -13.7) |
| [[Hs 766T (line)]] | wt | 20.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.16× (z +9.3) | — |
| [[HS-578T (line)]] | alt | 34.7 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.311× (z -11.1) |
| [[hTERT-HPNE (line)]] | wt | 32.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.47× (z +9.1) | — |
| [[KATO III (line)]] | alt | 24.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.87× (z +10.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 12.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.94× (z +8.8) | — |
| [[NCI-H1792 (line)]] | alt | 21.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.48× (z +15.5) | — |
| [[NCI-H2347 (line)]] | alt | 10.0 | 1 | 0 | [[Auranofin (drug)]] 5 µM 5.77× (z +9.5) | — |
| [[NCI-H460 (line)]] | wt | 18.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.83× (z +8.7) | — |
| [[SK-MEL-2 (line)]] | alt | 15.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.87× (z +9.8) | — |
| [[SNU-423 (line)]] | alt | 17.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.43× (z +9.1) | — |
| [[SW480 (line)]] | alt | 18.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +8.6) | — |
| [[A-427 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 28.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.88 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 30.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.04 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 25.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.43 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 21.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.92 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 52.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 16.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11835), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C6orf62]] | +0.63 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[FLACC1]] | +0.61 | +0.63 / +0.51 | both halves | 1e-05 |  |
| [[TLCD2]] | +0.60 | +0.57 / +0.58 | both halves | 1e-05 | ⚠ same locus (1.1 kb, same strand: neighbours can correlate without regulation) |
| [[THUMPD3-AS1]] | +0.60 | +0.57 / +0.64 | both halves | 1e-05 |  |
| [[SRP19]] | +0.60 | +0.63 / +0.49 | both halves | 1e-05 |  |
| [[ZNF432]] | +0.60 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[TMEM217]] | +0.60 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[ORAI2]] | +0.59 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[GABRR2]] | +0.59 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[SLC9A5]] | +0.58 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[VPS9D1]] | +0.58 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[LINC02798]] | +0.58 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[MON1B]] | +0.58 | +0.56 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KDM1A]] | -0.62 | -0.64 / -0.58 | both halves | 7e-06 |  |
| [[SKP2]] | -0.62 | -0.64 / -0.63 | both halves | 7e-06 |  |
| [[CTDSPL2]] | -0.61 | -0.63 / -0.54 | both halves | 1e-05 |  |
| [[LDHB]] | -0.59 | -0.59 / -0.47 | both halves | 2e-05 |  |
| [[PTCD3]] | -0.58 | -0.37 / -0.69 | both halves | 9e-05 |  |
| [[KCTD3]] | -0.58 | -0.46 / -0.70 | both halves | 2e-05 |  |
| [[SDHAF3]] | -0.57 | -0.59 / -0.56 | both halves | 1e-05 |  |
| [[HADH]] | -0.56 | -0.58 / -0.50 | both halves | 1e-05 |  |
| [[CDCA7L]] | -0.56 | -0.53 / -0.60 | both halves | 1e-05 |  |
| [[HAUS1]] | -0.56 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[ALDH7A1]] | -0.55 | -0.45 / -0.64 | both halves | 3e-05 |  |
| [[NDC1]] | -0.55 | -0.68 / -0.39 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMEM92-AS1]] | B | TMEM92-AS1 activity raises MIR22HG's level | lines that do not express TMEM92-AS1 (16) vs lines expressing it (34) | 1.88× lower at baseline in the lines without TMEM92-AS1 | 0.006 | ⚠ within organs, on part of the lines; also absent: CXCL8, SPTLC3, PLOD2 |
| [[FER1L4]] | B | FER1L4 activity raises MIR22HG's level | lines that do not express FER1L4 (7) vs lines expressing it (43) | 1.31× lower at baseline in the lines without FER1L4 | 0.041 | ⚠ within organs, on part of the lines; also absent: TNFRSF10A, STEAP2, OSR2; maybe low, not absent |
| [[ALDH5A1]] | B | ALDH5A1 activity lowers MIR22HG's level | lines that do not express ALDH5A1 (7) vs lines expressing it (43) | 1.61× higher at baseline in the lines without ALDH5A1 | 0.060 | ⚠ within organs, on part of the lines; also absent: CMTM8, CXCL16, PRKCZ; its own permutation p |
| [[CACNG8]] | B | CACNG8 activity raises MIR22HG's level | lines that do not express CACNG8 (14) vs lines expressing it (36) | 1.40× lower at baseline in the lines without CACNG8 | 0.067 | ⚠ within organs, on part of the lines; also absent: CACNG6, GAB3, KHDC1 |
| [[TMEM92-AS1]] | B | TMEM92-AS1 activity strengthens MIR22HG's drug response | lines that do not express TMEM92-AS1 (16) vs lines expressing it (32) | the lines without TMEM92-AS1 respond 0.79× as strongly (z diff +0.59); strongest at Niclosamide (olamine) 5 µM: 0.94x vs 0.55x (z diff +2.9) | 0.090 | ⚠ within organs, on part of the lines; also absent: CXCL8, SPTLC3, PLOD2; target measured in part of the lines; the reference differs; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 038]]; 122 genes; every member is in the + arm (projection on the module's main direction 0.609). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (31.1, -22.0); signed map (9.5, 12.3). **Vector** length 127, 35.5% of its response variance represented; |z| ≥ 3 in 1,040 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +10.0 | +12.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +8.9 | +12.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +8.0 | +9.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.2 | +6.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM |  | +3.9 | +4.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.5 | +4.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.8 | +1.5 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | +2.7 | +2.5 |
|  | [[Pralsetinib (drug)]] 0.05 µM |  | +2.3 | +1.6 |
| fall | [[Selinexor (drug)]] 5 µM |  | -5.4 | -6.1 |
|  | [[Radotinib (drug)]] 5 µM |  | -4.3 | -4.6 |
|  | [[NG25 (drug)]] 5 µM |  | -4.3 | -5.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.2 | -5.3 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -4.2 | -5.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.7 | -3.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | -3.6 | -3.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.5 | -5.5 |

## What is on record

|  |  |
|---|---|
| Name | MIR22 host gene |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 17p13.3 — chr17:1,711,447-1,717,174 (-) |
| Ensembl biotype | lncRNA |
| Also known as | MGC14376, DKFZp686O06159; previously C17orf91 |
| Gene groups (HGNC) | MicroRNA non-coding host genes |
| Matched by | ensembl_id |

UniProt [Q0VDD5](https://www.uniprot.org/uniprotkb/Q0VDD5) carries no function annotation.

**Summary**, from NCBI Gene [84981](https://www.ncbi.nlm.nih.gov/gene/84981):

> Predicted to act upstream of or within response to wounding. Predicted to be part of RISC complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28219](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28219) · Entrez [84981](https://www.ncbi.nlm.nih.gov/gene/84981) · UniProt [Q0VDD5](https://www.uniprot.org/uniprotkb/Q0VDD5) · Ensembl [ENSG00000186594](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000186594)

## Data

Gene col 11835: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11835); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11835, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11835]; `tensor/DDL_lfc|DDL_z.npy` [11835]; `embed/gene_vectors.npy` [11835]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11835 or target_col == 11835). Every well: [[MIR22HG — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MIR22HG.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
