---
symbol: "PA2G4"
type: "gene"
col: 9966
ensembl_id: "ENSG00000170515"
name: "proliferation-associated 2G4"
location: "12q13.2"
module: 5
arm: "+"
pooled_cpm: 140.77
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 0
n_dd_up_clean: 6
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# PA2G4

*proliferation-associated 2G4* — 12q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (14 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.97× (z +12.7, q 3e-34, up in 49 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.60× (z +3.7, q 0.013, up in 28 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Atazanavir (sulfate) (drug)]] 0.05 µM in 1 line (NCI-H596 0.182×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DHX33]] (+0.74, fdr 7e-06), [[URB2]] (+0.70, fdr 7e-06), [[NME1]] (+0.70, fdr 7e-06); moves opposite to [[OSER1-DT]] (-0.62, fdr 1e-05), [[FAM117A]] (-0.62, fdr 1e-05), [[CDKN1C]] (-0.59, fdr 2e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 14 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9966.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **4.97×** | +12.7 | 3e-34 | 49/49 (NCI-H1792, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **4.49×** | +11.4 | 7e-28 | 43/44 (SNU-423, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **3.02×** | +8.1 | 9e-14 | 45/45 (SNU-423, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.55×** | +7.1 | 1e-10 | 46/47 (MIA PaCa-2, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~49% of this change | **2.03×** | +5.4 | 7e-06 | 43/47 (LoVo, C32, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.73×** | +4.3 | 0.001 | 42/48 (NCI-H1792, SW480, …) | two highest doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.45×** | +4.1 | 0.003 | 32/49 (A549, NCI-H2347, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~69% of this change | **1.66×** | +4.0 | 0.004 | 44/48 (PANC-1, HT-29, …) | inconsistent across doses | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **1.60×** | +3.7 | 0.013 | 28/48 (MIA PaCa-2, SW480, …) | top dose only | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.57×** | +3.6 | 0.020 | 38/48 (NCI-H1792, SW 900, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.56×** | +3.6 | 0.020 | 32/48 (HOP62, SW 900, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.59×** | +3.5 | 0.020 | 31/48 (A-172, SNU-423, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.57×** | +3.4 | 0.025 | 28/48 (NCI-H1792, A549, …) | two highest doses | composition shift |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~83% of this change | **1.34×** | +3.3 | 0.040 | 41/48 (HT-29, SW48, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.50×** | +3.2 | 0.052 | 32/48 (SNU-423, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.50×** | +3.1 | 0.068 | 28/48 (NCI-H1792, C32, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **2.10×** | +3.1 | 0.068 | 35/48 (NCI-H460, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **2.05×** | +3.0 | 0.084 | 35/48 (AsPC-1, NCI-H460, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9966.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Atazanavir (sulfate) (drug)]] 0.05 µM in 1 line (NCI-H596 0.182×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | 0.724× | -3.6 | 0.17 | 42/48 (SW1417, A-427, …) | all doses, flat |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.875× | -3.4 | 0.18 | 6/50 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM |  | 0.744× | -3.3 | 0.18 | 27/48 (SNU-1, A-427, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[GSK1059615 (drug)]] 5 µM |  | 0.471× | -3.1 | 0.26 | 36/49 (LS 180, A-427, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Anethole trithione (drug)]] 0.5 µM |  | 0.684× | -3.0 | 0.30 | 41/48 (SNU-423, HOP62, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.63 per unit of S-phase module lfc, +0.53 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9966. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 53.6 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 14.0× (z +14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[A498 (line)]] | wt | 154 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.63× (z +12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[A549 (line)]] | wt | 115 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.52× (z +12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[Hs 766T (line)]] | wt | 97.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.82× (z +12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[HS-578T (line)]] | alt | 94.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.93× (z +12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[HT-29 (line)]] | alt | 99.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.99× (z +13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 99.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.99× (z +12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[RPMI-7951 (line)]] | alt | 88.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.75× (z +11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[SNU-423 (line)]] | alt | 99.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.83× (z +14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[AsPC-1 (line)]] | alt | 85.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.12× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | — |
| [[C32 (line)]] | wt | 85.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.61× (z +11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[CFPAC-1 (line)]] | alt | 80.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.26× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[H4 (line)]] | wt | 93.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.61× (z +11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[HCT15 (line)]] | alt | 147 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.26× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[HOP62 (line)]] | alt | 64.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.06× (z +12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[J82 (line)]] | alt | 173 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.69× (z +11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[LoVo (line)]] | wt | 176 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.30× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[LOX-IMVI (line)]] | wt | 176 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.67× (z +11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[LS 180 (line)]] | wt | 149 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.79× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[NCI-H1573 (line)]] | alt | 96.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 8.47× (z +11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | — |
| [[NCI-H2347 (line)]] | alt | 122 | 2 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.59× (z +9.8) ⚠ cell-cycle shift, explains ~35% of this change | — |
| [[NCI-H460 (line)]] | wt | 144 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.54× (z +14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[PANC-1 (line)]] | alt | 159 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.85× (z +12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 159 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.27× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[SW 900 (line)]] | alt | 72.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.62× (z +12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | — |
| [[SW480 (line)]] | alt | 226 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.21× (z +11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[A-172 (line)]] | wt | 91.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.41× (z +11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[A-427 (line)]] | wt | 299 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.79× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[AN3 CA (line)]] | alt | 165 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.67× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[COLO 205 (line)]] | alt | 71.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.88× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[HepG2_C3A (line)]] | wt | 120 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.23× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 90.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.45× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[KATO III (line)]] | alt | 114 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.31× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[NCI-H23 (line)]] | alt | 258 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.36× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[NCI-H596 (line)]] | alt | 133 | 0 | 1 | — | [[Atazanavir (sulfate) (drug)]] 0.05 µM 0.182× (z -8.6) |
| [[Panc 03.27 (line)]] | alt | 142 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.86× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[SW1417 (line)]] | alt | 146 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.20× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | — |
| [[BT-474 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 184 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 148 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 147 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 204 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 98.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 224 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 276 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 175 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 123 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 79.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 195 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9966), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DHX33]] | +0.74 | +0.72 / +0.66 | both halves | 7e-06 |  |
| [[URB2]] | +0.70 | +0.73 / +0.65 | both halves | 7e-06 |  |
| [[NME1]] | +0.70 | +0.74 / +0.63 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[LYAR]] | +0.69 | +0.70 / +0.68 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 861 |
| [[WDR43]] | +0.68 | +0.71 / +0.66 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V2; STRING 733 |
| [[TCOF1]] | +0.68 | +0.71 / +0.61 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V2 |
| [[DKC1]] | +0.67 | +0.75 / +0.59 | both halves | 7e-06 | STRING 911 |
| [[POLR1A]] | +0.66 | +0.65 / +0.63 | both halves | 7e-06 | STRING 876 |
| [[NOP16]] | +0.65 | +0.67 / +0.64 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V1 |
| [[PINX1]] | +0.64 | +0.64 / +0.57 | both halves | 9e-06 |  |
| [[RANBP1]] | +0.64 | +0.69 / +0.65 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 458 |
| [[TOMM40]] | +0.64 | +0.68 / +0.57 | both halves | 9e-06 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OSER1-DT]] | -0.62 | -0.53 / -0.58 | both halves | 1e-05 |  |
| [[FAM117A]] | -0.62 | -0.59 / -0.56 | both halves | 1e-05 |  |
| [[CDKN1C]] | -0.59 | -0.61 / -0.46 | both halves | 2e-05 |  |
| [[HDAC5]] | -0.58 | -0.66 / -0.50 | both halves | 1e-05 | STRING 401 |
| [[WBP1]] | -0.58 | -0.62 / -0.51 | both halves | 1e-05 |  |
| [[NEU1]] | -0.58 | -0.62 / -0.44 | both halves | 3e-05 |  |
| [[PNPLA2]] | -0.56 | -0.50 / -0.46 | both halves | 2e-05 |  |
| [[TP53INP2]] | -0.55 | -0.58 / -0.42 | both halves | 4e-05 |  |
| [[UBXN6]] | -0.55 | -0.49 / -0.54 | both halves | 1e-05 |  |
| [[CLIP3]] | -0.54 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[AAMDC]] | -0.54 | -0.60 / -0.45 | both halves | 3e-05 |  |
| [[SIRT2]] | -0.54 | -0.74 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.649). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-13.3, -38.5); signed map (-4.8, -49.1). **Vector** length 69.8, 33.2% of its response variance represented; |z| ≥ 3 in 997 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.8 | +3.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.7 | +2.1 |
|  | [[EX229 (drug)]] 5 µM |  | +2.8 | +3.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.7 | +2.5 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +2.6 | +1.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.4 | +2.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.4 | -0.1 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -4.5 | -3.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | -3.7 | +12.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | -3.3 | +11.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | -2.5 | +8.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | -2.1 | +1.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.1 | -1.4 |
|  | [[Entrectinib (drug)]] 5 µM |  | -1.8 | +0.3 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | -1.7 | +1.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.7 | +1.0 |

## What is on record

|  |  |
|---|---|
| Name | proliferation-associated 2G4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.2 — chr12:56,104,537-56,113,910 (+) |
| Ensembl biotype | protein_coding |
| Also known as | EBP1, ITAF45 |
| Gene groups (HGNC) | M24 metallopeptidase family |
| Hallmark sets | MYC_TARGETS_V2, ANDROGEN_RESPONSE, E2F_TARGETS, MYC_TARGETS_V1 |
| Reactome | 2 pathways, smallest: Neutrophil degranulation; Innate Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UQ80](https://www.uniprot.org/uniprotkb/Q9UQ80) (Proliferation-associated protein 2G4):

> May play a role in a ERBB3-regulated signal transduction pathway. Seems be involved in growth regulation. Acts a corepressor of the androgen receptor (AR) and is regulated by the ERBB3 ligand neuregulin-1/heregulin (HRG). Inhibits transcription of some E2F1-regulated promoters, probably by recruiting histone acetylase (HAT) activity. Binds RNA. Associates with 28S, 18S and 5.8S mature rRNAs, several rRNA precursors and probably U3 small nucleolar RNA. May be involved in regulation of …

**Summary**, from NCBI Gene [5036](https://www.ncbi.nlm.nih.gov/gene/5036):

> This gene encodes an RNA-binding protein that is involved in growth regulation. This protein is present in pre-ribosomal ribonucleoprotein complexes and may be involved in ribosome assembly and the regulation of intermediate and late steps of rRNA processing. This protein can interact with the cytoplasmic domain of the ErbB3 receptor and may contribute to transducing growth regulatory signals. This protein is also a transcriptional co-repressor of androgen receptor-regulated genes and other …

**Accessions** — [HGNC:8550](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8550) · Entrez [5036](https://www.ncbi.nlm.nih.gov/gene/5036) · UniProt [Q9UQ80](https://www.uniprot.org/uniprotkb/Q9UQ80) · Ensembl [ENSG00000170515](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170515)

## Data

Gene col 9966: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9966); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9966, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9966]; `tensor/DDL_lfc|DDL_z.npy` [9966]; `embed/gene_vectors.npy` [9966]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9966 or target_col == 9966). Every well: [[PA2G4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PA2G4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
