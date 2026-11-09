---
symbol: "RPS18"
type: "gene"
col: 13796
ensembl_id: "ENSG00000231500"
name: "ribosomal protein S18"
location: "6p21.32"
module: 20
arm: "+"
pooled_cpm: 62.17
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 2
n_dd_up_clean: 12
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# RPS18

*ribosomal protein S18* — 6p21.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.78× (z +10.8, q 1e-24, up in 40 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 1.55× (z +4.8, q 2e-04, up in 41 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Ribociclib (drug)]] 0.05 µM: 0.499× (z -7.7, q 8e-12, down in 48 of 48 measured lines) ⚠ unreliable plate only; position not correctable. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 1 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[XRK3F2 (drug)]] 0.5 µM in 1 line (SK-MEL-2 0.0630×); [[Citalopram (hydrobromide) (drug)]] 0.5 µM in 1 line (NCI-H661 0.0735×); [[Isocorydine (drug)]] 0.5 µM in 1 line (CHP-212 0.160×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPL3]] (+0.86, fdr 7e-06), [[RPL4]] (+0.83, fdr 7e-06), [[RPL18A]] (+0.82, fdr 7e-06); moves opposite to [[EID2]] (-0.60, fdr 1e-05), [[C14orf119]] (-0.59, fdr 1e-05), [[IRX5]] (-0.58, fdr 1e-05).
> It sits in the **+** arm of [[Module 020]] (Cap-dependent Translation Initiation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CRTAP]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13796.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.78×** | +10.8 | 1e-24 | 40/44 (SW480, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.63×** | +10.7 | 4e-24 | 44/49 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.48×** | +9.3 | 3e-18 | 44/45 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.20×** | +7.0 | 5e-10 | 26/50 (LoVo, Panc 03.27, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.55×** | +4.8 | 2e-04 | 41/48 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.54×** | +4.7 | 2e-04 | 42/47 (SW 900, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~9% here) |
| [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM |  | **1.59×** | +4.7 | 2e-04 | 39/47 (LoVo, SW480, …) | inconsistent across doses | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.55×** | +4.6 | 3e-04 | 34/47 (NCI-H1573, SW 900, …) | top dose only | cell-cycle shift (explains ~11% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.46×** | +4.2 | 0.002 | 35/48 (NCI-H1792, HT-29, …) | inconsistent across doses | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.45×** | +4.1 | 0.002 | 31/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.43×** | +3.9 | 0.005 | 32/48 (HT-29, KATO III, …) | two highest doses |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **1.42×** | +3.8 | 0.006 | 34/48 (PANC-1, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Erlotinib (drug)]] 5 µM |  | **1.40×** | +3.6 | 0.016 | 29/47 (RPMI-7951, HT-29, …) | rises with dose | position effect removed |
| [[NG25 (drug)]] 5 µM |  | **1.80×** | +3.4 | 0.029 | 28/47 (HepG2/C3A, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~1% here); noisy plate (z scaled); position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **1.37×** | +3.3 | 0.037 | 27/49 (COLO 205, A549, …) | top dose only |  |
| [[Methotrexate (drug)]] 0.5 µM |  | **1.35×** | +3.3 | 0.038 | 25/48 (LoVo, HS-578T, …) | inconsistent across doses | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.24×** | +3.0 | 0.077 | 26/48 (HCT15, CFPAC-1, …) | top dose only | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.34×** | +3.0 | 0.077 | 23/48 (HT-29, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.33×** | +3.0 | 0.080 | 23/50 (A-427, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~13% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13796.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 1 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[XRK3F2 (drug)]] 0.5 µM in 1 line (SK-MEL-2 0.0630×); [[Citalopram (hydrobromide) (drug)]] 0.5 µM in 1 line (NCI-H661 0.0735×); [[Isocorydine (drug)]] 0.5 µM in 1 line (CHP-212 0.160×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.499×** | -7.7 | 8e-12 | 48/48 (NCI-H460, PANC-1, …) | inconsistent across doses |  |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.574×** | -6.1 | 2e-07 | 45/49 (SW480, NCI-H460, …) | inconsistent across doses |  |
| [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.5 µM |  | 0.743× | -3.3 | 0.18 | 31/47 (A549, BT-474, …) | inconsistent across doses | position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | 0.794× | -3.2 | 0.18 | 23/48 (SW480, RKO, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13796. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 57.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.04× (z +9.0) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 65.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.43× (z +12.1) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 40.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.25× (z +8.9) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 63.9 | 0 | 2 | — | [[Isocorydine (drug)]] 0.5 µM 0.160× (z -9.4) |
| [[HOP62 (line)]] | alt | 59.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.76× (z +10.2) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 45.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.73× (z +9.3) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 62.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.07× (z +10.9) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 102 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.57× (z +11.7) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 74.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.08× (z +8.7) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 34.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.98× (z +13.3) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 64.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.59× (z +11.5) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 58.7 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.293× (z -9.3) ⚠ cell-cycle shift, explains ~10% of this change |
| [[C-33 A (line)]] | alt | 78.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.59× (z +9.2) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 79.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.24× (z +8.6) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 53.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.71× (z +8.6) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 94.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.18× (z +8.7) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 47.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.03× (z +9.5) ⚠ toxic; transcription drop | — |
| [[NCI-H661 (line)]] | alt | 63.0 | 0 | 1 | — | [[Citalopram (hydrobromide) (drug)]] 0.5 µM 0.0735× (z -10.0) |
| [[PANC-1 (line)]] | alt | 63.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.82× (z +9.3) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 48.6 | 0 | 1 | — | [[XRK3F2 (drug)]] 0.5 µM 0.0630× (z -13.2) |
| [[SW 900 (line)]] | alt | 49.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.22× (z +8.6) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 30.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 45.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 92.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 52.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 49.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 39.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 54.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 46.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 52.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 80.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 57.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 40.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 101 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 71.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 57.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 81.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 65.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 74.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 91.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 94.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 46.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 56.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 86.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 75.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 47.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 53.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 61.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 115 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13796), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPL3]] | +0.86 | +0.87 / +0.85 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL4]] | +0.83 | +0.79 / +0.81 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL18A]] | +0.82 | +0.77 / +0.79 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL10]] | +0.81 | +0.77 / +0.81 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS3A]] | +0.80 | +0.80 / +0.79 | both halves | 7e-06 | same gene group; pathway: Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S; STRING 999 |
| [[ANKRD30BL]] | +0.78 | +0.77 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[RPL29]] | +0.77 | +0.86 / +0.64 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[EEF1A1P5]] | +0.76 | +0.74 / +0.79 | both halves | 7e-06 | pathway: Eukaryotic Translation Elongation |
| [[EEF1A1]] | +0.76 | +0.75 / +0.80 | both halves | 7e-06 | pathway: Eukaryotic Translation Elongation; STRING 986 |
| [[RPL14]] | +0.74 | +0.74 / +0.71 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[EEF1G]] | +0.70 | +0.79 / +0.60 | both halves | 7e-06 | pathway: Eukaryotic Translation Elongation; STRING 970 |
| [[HFM1]] | +0.69 | +0.67 / +0.64 | both halves | 7e-06 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EID2]] | -0.60 | -0.55 / -0.60 | both halves | 1e-05 |  |
| [[C14orf119]] | -0.59 | -0.50 / -0.64 | both halves | 1e-05 |  |
| [[IRX5]] | -0.58 | -0.49 / -0.56 | both halves | 1e-05 |  |
| [[PHACTR4]] | -0.55 | -0.49 / -0.56 | both halves | 1e-05 |  |
| [[DCP1A]] | -0.55 | -0.34 / -0.59 | both halves | 1e-04 | pathway: Nonsense Mediated Decay (NMD) enhanced by the Exon Junction Complex (EJC); STRING 534 |
| [[RBX1]] | -0.55 | -0.43 / -0.57 | both halves | 3e-05 | pathway: Regulation of expression of SLITs and ROBOs |
| [[PDCD7]] | -0.54 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[PIGBOS1]] | -0.54 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[ZNF503]] | -0.54 | -0.56 / -0.49 | both halves | 1e-05 |  |
| [[TMEM70]] | -0.54 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[ZCCHC10]] | -0.54 | -0.43 / -0.66 | both halves | 3e-05 |  |
| [[AP5S1]] | -0.54 | -0.56 / -0.56 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CRTAP]] | C | CRTAP activity raises RPS18's level | lines that do not express CRTAP (4) vs lines expressing it (46) | 1.46× lower at baseline in the lines without CRTAP | 0.048 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SACS, EPB41L2, KCNC4; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **+** arm (projection on the module's main direction 0.630). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-28.9, -25.5); signed map (-21.7, -34.2). **Vector** length 103, 28.3% of its response variance represented; |z| ≥ 3 in 733 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.7 | +9.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.6 | +10.8 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | +3.2 | +1.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.2 | +10.7 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | +3.2 | +2.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.1 | +3.0 |
|  | [[Hydroxyurea (drug)]] 5 µM |  | +2.7 | +0.5 |
|  | [[Artesunate (drug)]] 0.05 µM |  | +2.6 | +0.8 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -6.5 | -3.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.2 | -1.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.5 | -0.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -4.3 | +0.6 |
|  | [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | -3.7 | -7.7 |
|  | [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | -3.4 | -2.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.8 | -1.5 |
|  | [[Arbutin (drug)]] 5 µM |  | -2.8 | -1.4 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | -2.6 | -2.2 |
|  | [[Bendamustine (drug)]] 5 µM |  | -2.5 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | ribosomal protein S18 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.32 — chr6:33,272,075-33,276,511 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KE3, KE-3, HKE3, S18, uS13; previously D6S218E |
| Gene groups (HGNC) | S ribosomal proteins |
| Reactome | 51 pathways, smallest: SARS-CoV-1 modulates host translation machinery; SARS-CoV-2 modulates host translation machinery; Formation of the ternary complex, and subsequently, the 43S complex |
| Matched by | ensembl_id |

**Function**, from UniProt [P62269](https://www.uniprot.org/uniprotkb/P62269) (Small ribosomal subunit protein uS13):

> Component of the small ribosomal subunit. The ribosome is a large ribonucleoprotein complex responsible for the synthesis of proteins in the cell.

**Summary**, from NCBI Gene [6222](https://www.ncbi.nlm.nih.gov/gene/6222):

> Ribosomes, the organelles that catalyze protein synthesis, consist of a small 40S subunit and a large 60S subunit. Together these subunits are composed of 4 RNA species and approximately 80 structurally distinct proteins. This gene encodes a ribosomal protein that is a component of the 40S subunit. The protein belongs to the S13P family of ribosomal proteins. It is located in the cytoplasm. The gene product of the E. coli ortholog (ribosomal protein S13) is involved in the binding of fMet-tRNA, …

**Accessions** — [HGNC:10401](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10401) · Entrez [6222](https://www.ncbi.nlm.nih.gov/gene/6222) · UniProt [P62269](https://www.uniprot.org/uniprotkb/P62269) · Ensembl [ENSG00000231500](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000231500)

## Data

Gene col 13796: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13796); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13796, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13796]; `tensor/DDL_lfc|DDL_z.npy` [13796]; `embed/gene_vectors.npy` [13796]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13796 or target_col == 13796). Every well: [[RPS18 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPS18.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
