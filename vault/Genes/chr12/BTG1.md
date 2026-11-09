---
symbol: "BTG1"
type: "gene"
col: 5460
ensembl_id: "ENSG00000133639"
name: "BTG anti-proliferation factor 1"
location: "12q21.33"
module: 20
arm: "-"
pooled_cpm: 167.65
n_lines_expressing: 49
n_dd_up: 10
n_dd_down: 11
n_dd_up_clean: 4
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 12
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# BTG1

*BTG anti-proliferation factor 1* — 12q21.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (6 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 1.95× (z +6.7, q 1e-08, up in 44 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.457× (z -7.2, q 5e-10, down in 33 of 42 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Budesonide (drug)]] 5 µM: 0.706× (z -3.5, q 0.042, down in 30 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SERTAD1]] (+0.69, fdr 7e-06), [[METTL23]] (+0.68, fdr 7e-06), [[ACAP1]] (+0.65, fdr 1e-05); moves opposite to [[SMPD4]] (-0.70, fdr 1e-05), [[NAA50]] (-0.69, fdr 7e-06), [[NADK]] (-0.66, fdr 7e-06).
> It sits in the **-** arm of [[Module 020]] (Cap-dependent Translation Initiation).
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[DUSP10]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 6 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5460.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **1.95×** | +6.7 | 1e-08 | 44/47 (NCI-H460, A549, …) | all doses, flat | cell-cycle shift (explains ~18% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.58×** | +6.5 | 2e-08 | 30/47 (A498, PANC-1, …) | all doses, flat | composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.90×** | +6.5 | 2e-08 | 39/47 (NCI-H460, A549, …) | all doses, flat | position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **1.70×** | +4.9 | 2e-04 | 33/47 (PANC-1, SW 900, …) | all doses, flat | composition shift |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.67×** | +4.8 | 2e-04 | 38/46 (NCI-H460, A549, …) | all doses, flat | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **1.59×** | +4.7 | 3e-04 | 29/47 (SW 900, PANC-1, …) | all doses, flat | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.51×** | +4.2 | 0.002 | 29/47 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.28×** | +3.5 | 0.031 | 25/47 (hTERT-HPNE, SW1417, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~84% of this change | **1.40×** | +3.4 | 0.039 | 29/47 (PANC-1, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **1.37×** | +3.2 | 0.076 | 24/47 (NCI-H1573, NCI-H460, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | 1.80× | +3.1 | 0.10 | 35/47 (NCI-H2347, SHP-77, …) | top dose only | noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | 1.52× | +3.0 | 0.12 | 31/47 (LoVo, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 7 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5460.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.457×** | -7.2 | 5e-10 | 33/42 (SW 900, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.546×** | -6.0 | 4e-07 | 35/48 (SNU-423, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.549×** | -5.5 | 9e-06 | 41/47 (LOX-IMVI, SNU-423, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.601×** | -5.1 | 5e-05 | 42/47 (A498, NCI-H2030, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.751×** | -4.0 | 0.006 | 32/48 (A549, SNU-423, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.656×** | -3.9 | 0.009 | 25/44 (SNU-423, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift; position effect removed |
| [[Budesonide (drug)]] 5 µM |  | **0.706×** | -3.5 | 0.042 | 30/47 (NCI-H1573, Panc 03.27, …) | top dose only | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.694×** | -3.3 | 0.062 | 28/49 (LOX-IMVI, SNU-423, …) | rises with dose |  |
| [[venetoclax (drug)]] 5 µM |  | **0.533×** | -3.3 | 0.062 | 28/47 (SHP-77, SW480, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[TAK-733 (drug)]] 5 µM |  | **0.538×** | -3.2 | 0.067 | 27/47 (NCI-H460, C32, …) | top dose only | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.716×** | -3.2 | 0.083 | 27/47 (HEC-1-A, C32, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.43 per unit of S-phase module lfc, +0.76 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5460. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 365 | 0 | 7 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.163× (z -14.0) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 402 | 4 (1 ⚠) | 2 (2 ⚠) | [[Harringtonine (drug)]] 0.5 µM 4.33× (z +13.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.343× (z -13.6) ⚠ cell-cycle shift, explains ~42% of this change |
| [[NCI-H460 (line)]] | wt | 201 | 6 (3 ⚠) | 0 | [[Harringtonine (drug)]] 0.5 µM 6.24× (z +15.8) | — |
| [[SNU-423 (line)]] | alt | 388 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.128× (z -15.6) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 128 | 4 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.75× (z +17.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 3.75× (z +12.2) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.353× (z -9.7) ⚠ unreliable plate only |
| [[NCI-H1573 (line)]] | alt | 375 | 5 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.45× (z +12.6) ⚠ cell-cycle shift, explains ~54% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 4.88× (z +11.8) | — |
| [[SW 900 (line)]] | alt | 134 | 4 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.43× (z +13.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 4.65× (z +12.2) | [[Dinaciclib (drug)]] 5 µM 0.113× (z -15.6) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 248 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.249× (z -11.7) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 130 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.24× (z +14.4) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 3.43× (z +10.6) | — |
| [[CFPAC-1 (line)]] | alt | 184 | 2 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +13.0) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 0.5 µM 0.401× (z -8.6) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 187 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.230× (z -11.9) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 134 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.03× (z +14.0) ⚠ cell-cycle shift, would explain all of this change | — |
| [[C32 (line)]] | wt | 149 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +10.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 3.18× (z +9.5) | — |
| [[J82 (line)]] | alt | 185 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.187× (z -12.1) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 132 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.227× (z -13.0) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 159 | 0 | 2 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.281× (z -9.6) ⚠ cell-cycle shift, explains ~27% of this change |
| [[SW480 (line)]] | alt | 159 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.260× (z -11.8) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 60.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +8.7) ⚠ cell-cycle shift, would explain all of this change | — |
| [[H4 (line)]] | wt | 140 | 1 | 0 | [[Homoharringtonine (drug)]] 0.05 µM 3.58× (z +8.8) | — |
| [[HepG2_C3A (line)]] | wt | 142 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +9.3) ⚠ cell-cycle shift, would explain all of this change | — |
| [[HOP62 (line)]] | alt | 259 | 1 | 0 | [[Harringtonine (drug)]] 0.5 µM 4.64× (z +10.3) | — |
| [[HT-29 (line)]] | alt | 161 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.306× (z -9.4) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 141 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +9.1) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H1792 (line)]] | alt | 312 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.294× (z -9.0) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 185 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.448× (z -10.1) ⚠ cell-cycle shift, explains ~42% of this change |
| [[Panc 03.27 (line)]] | alt | 158 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +9.4) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SW1417 (line)]] | alt | 145 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +8.6) ⚠ cell-cycle shift, would explain all of this change | — |
| [[A-172 (line)]] | wt | 129 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 70.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 57.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 51.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 125 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 158 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 81.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 94.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 136 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 193 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 77.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 310 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 72.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 188 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 41.6 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 76.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 158 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 99.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 57.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 155 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 223 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 76.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5460), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*43 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SERTAD1]] | +0.69 | +0.65 / +0.69 | both halves | 7e-06 |  |
| [[METTL23]] | +0.68 | +0.58 / +0.65 | both halves | 7e-06 |  |
| [[ACAP1]] | +0.65 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[CTR9]] | +0.64 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[ANKRD12]] | +0.63 | +0.58 / +0.61 | both halves | 7e-06 |  |
| [[MED19]] | +0.63 | +0.47 / +0.61 | both halves | 2e-05 |  |
| [[FAM43A]] | +0.63 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[NOSIP]] | +0.63 | +0.58 / +0.57 | both halves | 9e-06 |  |
| [[ADM]] | +0.63 | +0.50 / +0.68 | both halves | 1e-05 | pathway: HALLMARK_HYPOXIA |
| [[IRF2BP2]] | +0.63 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[MARCKS]] | +0.63 | +0.59 / +0.66 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[C15orf48]] | +0.63 | +0.54 / +0.64 | both halves | 1e-05 |  |

## Genes that move opposite

*57 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMPD4]] | -0.70 | -0.52 / -0.69 | both halves | 1e-05 |  |
| [[NAA50]] | -0.69 | -0.61 / -0.67 | both halves | 7e-06 |  |
| [[NADK]] | -0.66 | -0.60 / -0.68 | both halves | 7e-06 |  |
| [[SENP3]] | -0.66 | -0.55 / -0.63 | both halves | 1e-05 |  |
| [[USP5]] | -0.65 | -0.60 / -0.62 | both halves | 7e-06 |  |
| [[EIF3F]] | -0.65 | -0.49 / -0.64 | both halves | 1e-05 |  |
| [[USP39]] | -0.65 | -0.55 / -0.64 | both halves | 1e-05 |  |
| [[GCN1]] | -0.64 | -0.48 / -0.74 | both halves | 2e-05 |  |
| [[LARP1]] | -0.64 | -0.58 / -0.63 | both halves | 7e-06 |  |
| [[LY6G5B]] | -0.64 | -0.43 / -0.64 | both halves | 3e-05 |  |
| [[EMC1]] | -0.63 | -0.42 / -0.70 | both halves | 4e-05 |  |
| [[MACROH2A1]] | -0.62 | -0.48 / -0.63 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 12, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DUSP10]] | B | DUSP10 activity raises BTG1's level | lines that do not express DUSP10 (11) vs lines expressing it (39) | 2.02× lower at baseline in the lines without DUSP10 | 0.004 | ⚠ within organs, on part of the lines; also absent: GLRX, GBP2, TMEM92-AS1; maybe low, not absent |
| [[C15orf48]] | B | C15orf48 activity raises BTG1's level | lines that do not express C15orf48 (25) vs lines expressing it (25) | 1.69× lower at baseline in the lines without C15orf48 | 0.025 | ⚠ within organs, on part of the lines; also absent: ZNF229, HMGN2P46, RHCG |
| [[FBXO32]] | B | FBXO32 activity raises BTG1's level | lines that do not express FBXO32 (14) vs lines expressing it (36) | 1.86× lower at baseline in the lines without FBXO32 | 0.026 | ⚠ within organs, on part of the lines; also absent: ETS2, BACE2, MLPH; maybe low, not absent |
| [[TLE4]] | B | TLE4 activity raises BTG1's level | lines that do not express TLE4 (10) vs lines expressing it (40) | 1.96× lower at baseline in the lines without TLE4 | 0.039 | ⚠ within organs, on part of the lines; also absent: LMO7, CA13, KITLG |
| [[GEM]] | B | GEM activity raises BTG1's level | lines that do not express GEM (9) vs lines expressing it (41) | 1.89× lower at baseline in the lines without GEM | 0.042 | ⚠ within organs, on part of the lines; also absent: PLSCR2, ALCAM, SHB |
| [[NEDD9]] | B | NEDD9 activity raises BTG1's level | lines that do not express NEDD9 (16) vs lines expressing it (34) | 1.62× lower at baseline in the lines without NEDD9 | 0.049 | ⚠ within organs, on part of the lines; also absent: ITGA1, LGALS3, DGKG |
| [[LTBR]] | B | LTBR activity raises BTG1's level | lines that do not express LTBR (8) vs lines expressing it (42) | 1.68× lower at baseline in the lines without LTBR | 0.057 | ⚠ within organs, on part of the lines; also absent: SIGIRR, YPEL3, CLCF1 |
| [[RND3]] | B | RND3 activity raises BTG1's level | lines that do not express RND3 (5) vs lines expressing it (45) | 2.25× lower at baseline in the lines without RND3 | 0.060 | ⚠ within organs, on part of the lines; also absent: GULP1, SFXN3, GALNT7; its own permutation p |
| [[PTGER4]] | B | PTGER4 activity raises BTG1's level | lines that do not express PTGER4 (12) vs lines expressing it (38) | 1.77× lower at baseline in the lines without PTGER4 | 0.060 | ⚠ within organs, on part of the lines; also absent: CFAP20DC, AMOTL1, GOLGA7B; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity raises BTG1's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[BCL11B]] | B | BCL11B activity raises BTG1's level | lines that do not express BCL11B (18) vs lines expressing it (32) | 1.73× lower at baseline in the lines without BCL11B | 0.076 | ⚠ within organs, on part of the lines; also absent: ENSG00000249111, HLA-V-1, ENSG00000272297; maybe low, not absent |
| [[TNFRSF1B]] | B | TNFRSF1B activity raises BTG1's level | lines that do not express TNFRSF1B (17) vs lines expressing it (33) | 1.54× lower at baseline in the lines without TNFRSF1B | 0.090 | ⚠ within organs, on part of the lines; also absent: GUCY1B2, DGKE, LYPD5 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **-** arm (projection on the module's main direction -0.687). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-18.7, -29.6); signed map (-3.7, 10.6). **Vector** length 153, 57.3% of its response variance represented; |z| ≥ 3 in 1,149 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +8.5 | +6.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +8.0 | +3.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +6.2 | +2.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +6.1 | +6.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | +5.7 | +4.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +4.2 | +4.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +4.1 | +3.1 |
|  | [[Adagrasib (drug)]] 5 µM |  | +3.6 | +2.0 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -8.4 | -7.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -8.1 | -3.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -7.9 | -6.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -7.4 | -5.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -6.8 | -2.1 |
|  | [[Budesonide (drug)]] 5 µM |  | -5.0 | -3.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | -4.8 | -3.2 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -4.7 | -2.5 |
|  | [[venetoclax (drug)]] 5 µM |  | -4.7 | -3.3 |
|  | [[EX229 (drug)]] 5 µM |  | -4.5 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | BTG anti-proliferation factor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q21.33 — chr12:92,140,278-92,145,846 (-) |
| Ensembl biotype | protein_coding |
| Also known as | APRO2 |
| Gene groups (HGNC) | BTG/Tob family |
| Hallmark sets | UV_RESPONSE_UP, INTERFERON_GAMMA_RESPONSE, HYPOXIA, TNFA_SIGNALING_VIA_NFKB, P53_PATHWAY |
| Reactome | 2 pathways, smallest: FOXO-mediated transcription of cell cycle genes; FOXO-mediated transcription |
| Matched by | ensembl_id |

**Function**, from UniProt [P62324](https://www.uniprot.org/uniprotkb/P62324) (Protein BTG1):

> Anti-proliferative protein.

**Summary**, from NCBI Gene [694](https://www.ncbi.nlm.nih.gov/gene/694):

> This gene is a member of an anti-proliferative gene family that regulates cell growth and differentiation. Expression of this gene is highest in the G0/G1 phases of the cell cycle and downregulated when cells progressed through G1. The encoded protein interacts with several nuclear receptors, and functions as a coactivator of cell differentiation. This locus has been shown to be involved in a t(8;12)(q24;q22) chromosomal translocation in a case of B-cell chronic lymphocytic leukemia. [provided …

**Accessions** — [HGNC:1130](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1130) · Entrez [694](https://www.ncbi.nlm.nih.gov/gene/694) · UniProt [P62324](https://www.uniprot.org/uniprotkb/P62324) · Ensembl [ENSG00000133639](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000133639)

## Data

Gene col 5460: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5460); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5460, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5460]; `tensor/DDL_lfc|DDL_z.npy` [5460]; `embed/gene_vectors.npy` [5460]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5460 or target_col == 5460). Every well: [[BTG1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BTG1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
