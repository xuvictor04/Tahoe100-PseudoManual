---
symbol: "PSPH"
type: "gene"
col: 7118
ensembl_id: "ENSG00000146733"
name: "phosphoserine phosphatase"
location: "7p11.2"
module: 63
arm: "+"
pooled_cpm: 18.01
n_lines_expressing: 49
n_dd_up: 25
n_dd_down: 8
n_dd_up_clean: 16
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/063"]
generated_by: "tahoemap"
---

# PSPH

*phosphoserine phosphatase* — 7p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.22× (z +17.5, q 0e+00, up in 21 of 25 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.83× (z +9.4, q 7e-19, up in 33 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.502× (z -10.8, q 3e-24, down in 33 of 47 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TARS1]] (+0.65, fdr 7e-06), [[PSAT1]] (+0.59, fdr 1e-05), [[TCEA1]] (+0.59, fdr 4e-05); moves opposite to [[TMEM50A]] (-0.56, fdr 2e-05), [[TOM1L2]] (-0.53, fdr 2e-05), [[HIC2]] (-0.52, fdr 4e-05).
> It is in [[Module 063]], a single-armed module (ISR ATF4).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 9 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7118.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.22×** | +17.5 | 0e+00 | 21/25 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.93×** | +16.8 | 0e+00 | 36/40 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.13×** | +10.9 | 2e-25 | 30/36 (HEC-1-A, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.83×** | +9.4 | 7e-19 | 33/46 (LoVo, HEC-1-A, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.76×** | +8.9 | 1e-16 | 31/47 (AsPC-1, A-172, …) | all doses, stronger at high dose | position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **1.66×** | +7.9 | 3e-13 | 27/47 (PANC-1, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.56×** | +6.9 | 4e-10 | 24/47 (A-172, PANC-1, …) | all doses, stronger at high dose | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.54×** | +6.8 | 1e-09 | 30/46 (SW480, HT-29, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM |  | **1.35×** | +6.7 | 1e-09 | 24/47 (A-427, RKO, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.43×** | +5.6 | 1e-06 | 19/46 (PANC-1, BT-474, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.36×** | +4.8 | 7e-05 | 12/47 (A-172, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **1.36×** | +4.8 | 7e-05 | 18/44 (HEC-1-A, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.36×** | +4.8 | 9e-05 | 21/45 (HS-578T, NCI-H2030, …) | inconsistent across doses |  |
| [[venetoclax (drug)]] 5 µM |  | **1.72×** | +4.4 | 4e-04 | 12/44 (SW480, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **1.33×** | +4.3 | 7e-04 | 17/42 (HEC-1-A, SNU-423, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.69×** | +4.3 | 7e-04 | 12/44 (HT-29, CFPAC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.31×** | +4.1 | 0.001 | 14/47 (SHP-77, SW480, …) | rises with dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **1.62×** | +3.9 | 0.003 | 7/44 (SW480, LoVo, …) | top dose only | noisy plate (z scaled) |
| [[Afatinib (drug)]] 5 µM |  | **1.27×** | +3.8 | 0.004 | 9/47 (PANC-1, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.26×** | +3.4 | 0.016 | 13/46 (MIA PaCa-2, NCI-H2030, …) | top dose only |  |
| [[Vitamin K4 (drug)]] 0.05 µM |  | **1.22×** | +3.1 | 0.053 | 5/47 (A-172, NCI-H2030, …) | inconsistent across doses |  |
| [[Abiraterone acetate (drug)]] 0.05 µM |  | **1.21×** | +3.0 | 0.076 | 3/47 (LoVo, PANC-1, …) | inconsistent across doses |  |
| [[Neratinib (drug)]] 5 µM |  | **1.21×** | +2.9 | 0.084 | 12/46 (HEC-1-A, LoVo, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7118.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.502×** | -10.8 | 3e-24 | 33/47 (PANC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.515×** | -10.4 | 8e-23 | 37/46 (A-427, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.540×** | -9.6 | 1e-19 | 33/45 (PANC-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.606×** | -7.8 | 6e-13 | 26/45 (A-172, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.674×** | -6.2 | 7e-08 | 21/45 (A-427, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.789×** | -3.7 | 0.019 | 17/47 (A-427, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.639×** | -3.7 | 0.020 | 12/44 (Hs 766T, LS 180, …) | top dose only | noisy plate (z scaled) |
| [[BAY1125976 (drug)]] 5 µM |  | **0.660×** | -3.4 | 0.047 | 5/47 (A498, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.37 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7118. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 23.1 | 2 (2 ⚠) | 5 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.52× (z +11.7) ⚠ toxic; transcription drop | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.226× (z -14.4) |
| [[A-427 (line)]] | wt | 32.5 | 0 | 6 (2 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.307× (z -13.3) |
| [[HepG2_C3A (line)]] | wt | 51.9 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.261× (z -11.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.178× (z -10.5) |
| [[HEC-1-A (line)]] | alt | 28.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 5.11× (z +12.6) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 16.9 | 0 | 3 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.135× (z -12.4) ⚠ toxic; cell-cycle shift, explains ~26% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.265× (z -8.5) |
| [[SW480 (line)]] | alt | 43.2 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.43× (z +16.0) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 0.5 µM 0.403× (z -10.2) |
| [[A498 (line)]] | wt | 38.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.58× (z +12.6) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 9.69 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.96× (z +9.6) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 25.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.127× (z -14.4) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 7.02 | 0 | 1 (1 ⚠) | — | [[Pimozide (drug)]] 0.5 µM 0.101× (z -8.7) ⚠ transcription drop |
| [[HT-29 (line)]] | alt | 16.1 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.218× (z -9.6) |
| [[J82 (line)]] | alt | 9.33 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.179× (z -8.5) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 19.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.26× (z +10.6) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 6.32 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.20× (z +9.1) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 5.99 | 0 | 1 | — | [[Cepharanthine (drug)]] 0.5 µM 0.0705× (z -9.5) |
| [[SHP-77 (line)]] | alt | 30.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.44× (z +9.6) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 20.4 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0697× (z -11.3) ⚠ cell-cycle shift, explains ~78% of this change |
| [[SW1417 (line)]] | alt | 19.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.07× (z +9.0) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 9.89 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.75 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.99 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 22.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.81 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.28 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 7.94 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.58 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.20 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 9.76 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.28 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 30.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7118), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TARS1]] | +0.65 | +0.58 / +0.67 | both halves | 7e-06 |  |
| [[PSAT1]] | +0.59 | +0.51 / +0.62 | both halves | 1e-05 | pathway: HALLMARK_MTORC1_SIGNALING; STRING 999 |
| [[TCEA1]] | +0.59 | +0.42 / +0.59 | both halves | 4e-05 | pathway: HALLMARK_MTORC1_SIGNALING |
| [[YARS1]] | +0.58 | +0.48 / +0.62 | both halves | 2e-05 | STRING 562 |
| [[PLRG1]] | +0.57 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[HSPA9]] | +0.57 | +0.45 / +0.61 | both halves | 3e-05 | pathway: HALLMARK_MTORC1_SIGNALING |
| [[LARS1]] | +0.56 | +0.54 / +0.53 | both halves | 1e-05 | pathway: Metabolism of amino acids and derivatives |
| [[AGPS]] | +0.56 | +0.38 / +0.55 | both halves | 6e-05 |  |
| [[GTF2H3]] | +0.55 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[IARS1]] | +0.54 | +0.42 / +0.57 | both halves | 4e-05 | pathway: Metabolism of amino acids and derivatives |
| [[NARS1]] | +0.54 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[SLC7A11]] | +0.54 | +0.49 / +0.54 | both halves | 1e-05 | pathway: HALLMARK_MTORC1_SIGNALING |

## Genes that move opposite

*23 of its nearest partners move opposite, 3 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM50A]] | -0.56 | -0.46 / -0.61 | both halves | 2e-05 |  |
| [[TOM1L2]] | -0.53 | -0.47 / -0.53 | both halves | 2e-05 |  |
| [[HIC2]] | -0.52 | -0.41 / -0.50 | both halves | 4e-05 |  |
| [[OST4]] | -0.50 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[MRPL51]] ⚠ | -0.49 | -0.45 / -0.43 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[EIF1B]] | -0.49 | -0.30 / -0.45 | both halves | 2e-04 |  |
| [[PDE6D]] | -0.48 | -0.31 / -0.42 | both halves | 2e-04 |  |
| [[CDC37L1]] | -0.48 | -0.17 / -0.50 | ⚠ one half (not replicated) | 0.001 |  |
| [[COX7A2]] ⚠ | -0.47 | -0.46 / -0.39 | both halves | 5e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[HLA-E]] | -0.47 | -0.27 / -0.48 | both halves | 3e-04 |  |
| [[STX12]] | -0.46 | -0.32 / -0.46 | both halves | 2e-04 |  |
| [[UBL5]] | -0.46 | -0.48 / -0.46 | both halves | 2e-05 |  |
| [[MIF]] | -0.46 | -0.49 / -0.41 | both halves | 4e-05 |  |
| [[COX17]] | -0.46 | -0.37 / -0.43 | both halves | 9e-05 |  |
| [[TAF5]] | -0.46 | -0.46 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 063]] — ISR ATF4; 77 genes; every member is in the + arm (projection on the module's main direction 0.516). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-18.7, 46.1); signed map (-15.7, 23.8). **Vector** length 81.3, 16.2% of its response variance represented; |z| ≥ 3 in 926 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.1 | +16.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.7 | +17.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.2 | +10.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.4 | +9.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | +4.5 | +4.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.7 | +7.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.1 | +4.3 |
|  | [[venetoclax (drug)]] 5 µM |  | +3.1 | +4.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.8 | +3.9 |
| fall | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -4.5 | -9.6 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -4.5 | -10.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -4.0 | -10.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.7 | -0.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.9 | -7.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.4 | -2.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.3 | -3.7 |
|  | [[AZD-8055 (drug)]] 0.5 µM |  | -1.3 | -2.4 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | -1.2 | -0.3 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.2 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | phosphoserine phosphatase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p11.2 — chr7:56,011,051-56,051,604 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously PSP |
| Gene groups (HGNC) | HAD Asp-based non-protein phosphatases |
| Hallmark sets | MTORC1_SIGNALING |
| Reactome | 2 pathways, smallest: Serine metabolism; Metabolism of amino acids and derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [P78330](https://www.uniprot.org/uniprotkb/P78330) (Phosphoserine phosphatase):

> Catalyzes the last irreversible step in the biosynthesis of L-serine from carbohydrates, the dephosphorylation of O-phospho-L-serine to L-serine. L-serine can then be used in protein synthesis, to produce other amino acids, in nucleotide metabolism or in glutathione synthesis, or can be racemized to D-serine, a neuromodulator. May also act on O-phospho-D-serine (Probable).

**Summary**, from NCBI Gene [5723](https://www.ncbi.nlm.nih.gov/gene/5723):

> The protein encoded by this gene belongs to a subfamily of the phosphotransferases. This encoded enzyme is responsible for the third and last step in L-serine formation. It catalyzes magnesium-dependent hydrolysis of L-phosphoserine and is also involved in an exchange reaction between L-serine and L-phosphoserine. Deficiency of this protein is thought to be linked to Williams syndrome. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:9577](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9577) · Entrez [5723](https://www.ncbi.nlm.nih.gov/gene/5723) · UniProt [P78330](https://www.uniprot.org/uniprotkb/P78330) · Ensembl [ENSG00000146733](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000146733)

## Data

Gene col 7118: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7118); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7118, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7118]; `tensor/DDL_lfc|DDL_z.npy` [7118]; `embed/gene_vectors.npy` [7118]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7118 or target_col == 7118). Every well: [[PSPH — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PSPH.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
