---
symbol: "BAZ2A"
type: "gene"
col: 1144
ensembl_id: "ENSG00000076108"
name: "bromodomain adjacent to zinc finger domain 2A"
location: "12q13.3"
module: 74
arm: "+"
pooled_cpm: 197.91
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 5
n_dd_up_clean: 5
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/074"]
generated_by: "tahoemap"
---

# BAZ2A

*bromodomain adjacent to zinc finger domain 2A* — 12q13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (6 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.42× (z +9.1, q 3e-17, up in 40 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.758× (z -7.3, q 2e-10, down in 40 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Belumosudil (drug)]] 5 µM: 0.779× (z -6.3, q 6e-08, down in 29 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KMT2A]] (+0.59, fdr 2e-05), [[TTC9C]] (+0.58, fdr 1e-05), [[TBC1D17]] (+0.57, fdr 1e-05); moves opposite to [[CTPS1]] (-0.64, fdr 1e-05), [[SLFNL1-AS1]] (-0.59, fdr 1e-05), [[SPOPL-DT]] (-0.56, fdr 1e-05).
> It is in [[Module 074]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PPARA]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 8 with an alert ⚠; shown: the 15 strongest. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1144.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.42×** | +9.1 | 3e-17 | 40/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.37×** | +8.2 | 5e-14 | 35/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.25×** | +7.8 | 2e-12 | 27/48 (PANC-1, A549, …) | top dose only | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.30×** | +6.9 | 7e-10 | 30/48 (PANC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.31×** | +6.7 | 2e-09 | 32/48 (PANC-1, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.31×** | +6.7 | 2e-09 | 28/48 (PANC-1, A549, …) | rises with dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **1.48×** | +5.4 | 6e-06 | 28/48 (RKO, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~36% of this change | **1.22×** | +5.2 | 1e-05 | 29/48 (LOX-IMVI, C32, …) | inconsistent across doses | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~9% of this change | **1.22×** | +5.2 | 1e-05 | 24/48 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.45×** | +5.1 | 2e-05 | 30/49 (PANC-1, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~7% of this change | **1.20×** | +4.8 | 1e-04 | 22/48 (PANC-1, NCI-H460, …) | rises with dose | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~3% of this change | 1.18× | +4.2 | 0.001 | 21/47 (PANC-1, LoVo, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.17× | +4.0 | 0.003 | 18/48 (PANC-1, C32, …) | rises with dose |  |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | 1.14× | +3.4 | 0.029 | 13/47 (A-427, SW 900, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.5 µM |  | 1.19× | +3.2 | 0.047 | 17/49 (PANC-1, A-427, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 7 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1144.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.758×** | -7.3 | 2e-10 | 40/48 (AsPC-1, NCI-H1573, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~35% of this change | **0.762×** | -6.8 | 3e-09 | 32/47 (NCI-H2347, CFPAC-1, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.779×** | -6.3 | 6e-08 | 29/48 (LS 180, NCI-H1573, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | 0.835× | -4.5 | 9e-04 | 22/44 (A498, RPMI-7951, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | 0.851× | -4.2 | 0.003 | 21/48 (A498, SK-MEL-2, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | 0.854× | -4.1 | 0.003 | 19/48 (A498, AsPC-1, …) | rises with dose |  |
| [[Esmolol (hydrochloride) (drug)]] 5 µM |  | 0.867× | -3.7 | 0.016 | 6/48 (CHP-212, HOP62, …) | top dose only | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | 0.844× | -3.7 | 0.016 | 16/48 (Panc 03.27, RKO, …) | rises with dose | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | 0.864× | -3.5 | 0.025 | 20/45 (SW 900, NCI-H2347, …) | all doses, flat | composition shift |
| [[Brimonidine (drug)]] 5 µM |  | 0.877× | -3.4 | 0.035 | 8/48 (LoVo, NCI-H1792, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.781×** | -3.4 | 0.037 | 17/48 (Panc 03.27, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.909× | -3.4 | 0.037 | 6/48 (A-172, HT-29, …) | top dose only |  |
| [[Busulfan (drug)]] 0.05 µM |  | 0.884× | -3.2 | 0.057 | 8/49 (C32, SW1417, …) | inconsistent across doses |  |
| [[Pralsetinib (drug)]] 5 µM |  | **0.801×** | -3.0 | 0.098 | 17/49 (NCI-H460, C-33 A, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, +0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1144. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 172 | 10 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.60× (z +32.3) ⚠ cell-cycle shift, explains ~54% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.34× (z +15.9) | — |
| [[A498 (line)]] | wt | 265 | 2 (2 ⚠) | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +12.6) ⚠ cell-cycle shift, explains ~54% of this change | [[Panobinostat (drug)]] 5 µM 0.466× (z -10.9) ⚠ cell-cycle shift, explains ~65% of this change |
| [[NCI-H2347 (line)]] | alt | 208 | 2 (2 ⚠) | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.58× (z +11.8) ⚠ cell-cycle shift, explains ~54% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.540× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[NCI-H460 (line)]] | wt | 180 | 5 (4 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 2.23× (z +13.0) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.94× (z +11.2) | — |
| [[A-427 (line)]] | wt | 238 | 4 (3 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 2.53× (z +13.5) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 1.86× (z +9.4) | — |
| [[SNU-1 (line)]] | wt | 173 | 3 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +10.7) ⚠ cell-cycle shift, explains ~54% of this change | [[Dinaciclib (drug)]] 5 µM 0.402× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[A549 (line)]] | wt | 189 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +19.5) ⚠ cell-cycle shift, explains ~54% of this change | — |
| [[C32 (line)]] | wt | 134 | 2 | 0 | [[Auranofin (drug)]] 5 µM 2.76× (z +13.1) | — |
| [[CFPAC-1 (line)]] | alt | 217 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.61× (z +11.1) ⚠ cell-cycle shift, explains ~54% of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.572× (z -9.2) ⚠ toxic; cell-cycle shift, explains ~35% of this change |
| [[LoVo (line)]] | wt | 224 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.77× (z +9.3) | — |
| [[NCI-H2030 (line)]] | alt | 164 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +12.7) ⚠ cell-cycle shift, explains ~54% of this change | — |
| [[AsPC-1 (line)]] | alt | 240 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.561× (z -8.9) ⚠ cell-cycle shift, would explain all of this change |
| [[COLO 205 (line)]] | alt | 187 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.438× (z -9.8) ⚠ cell-cycle shift, explains ~33% of this change |
| [[H4 (line)]] | wt | 208 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.399× (z -9.6) ⚠ cell-cycle shift, would explain all of this change |
| [[J82 (line)]] | alt | 167 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.76× (z +11.0) ⚠ cell-cycle shift, explains ~54% of this change | — |
| [[LOX-IMVI (line)]] | wt | 191 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.61× (z +10.0) ⚠ cell-cycle shift, explains ~54% of this change | — |
| [[NCI-H23 (line)]] | alt | 266 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.68× (z +12.0) ⚠ cell-cycle shift, explains ~54% of this change | — |
| [[RKO (line)]] | wt | 280 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 3.39× (z +9.0) | — |
| [[RPMI-7951 (line)]] | alt | 169 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.443× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[SK-MEL-2 (line)]] | alt | 185 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.540× (z -8.8) ⚠ cell-cycle shift, would explain all of this change |
| [[SNU-423 (line)]] | alt | 163 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +13.2) ⚠ cell-cycle shift, explains ~54% of this change | — |
| [[SW 900 (line)]] | alt | 210 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.500× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[A-172 (line)]] | wt | 167 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 163 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 201 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 147 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 225 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 268 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 197 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 210 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 131 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 177 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 125 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 243 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 162 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 161 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 184 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 153 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 239 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 124 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 207 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 195 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 358 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 288 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 149 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 175 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 263 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 239 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 178 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 253 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1144), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*61 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KMT2A]] | +0.59 | +0.48 / +0.63 | both halves | 2e-05 | same gene group; pathway: Epigenetic regulation of gene expression |
| [[TTC9C]] | +0.58 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[TBC1D17]] | +0.57 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[TSC22D4]] | +0.57 | +0.64 / +0.50 | both halves | 1e-05 |  |
| [[WBP2]] | +0.56 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[MVP]] | +0.56 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[FOXO4]] | +0.56 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[MKRN1]] | +0.56 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[KLC4]] | +0.55 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[UBR2]] | +0.55 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[YPEL2]] | +0.54 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[UBXN6]] | +0.54 | +0.52 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*39 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CTPS1]] | -0.64 | -0.66 / -0.57 | both halves | 1e-05 |  |
| [[SLFNL1-AS1]] | -0.59 | -0.61 / -0.54 | both halves | 1e-05 |  |
| [[SPOPL-DT]] | -0.56 | -0.60 / -0.56 | both halves | 1e-05 |  |
| [[WDR4]] | -0.55 | -0.48 / -0.57 | both halves | 2e-05 |  |
| [[EEFSEC]] | -0.55 | -0.56 / -0.58 | both halves | 1e-05 |  |
| [[XXYLT1]] | -0.55 | -0.52 / -0.60 | both halves | 1e-05 |  |
| [[ZNF124]] | -0.55 | -0.51 / -0.63 | both halves | 1e-05 |  |
| [[CMSS1]] | -0.54 | -0.55 / -0.53 | both halves | 1e-05 |  |
| [[ARMC6]] | -0.53 | -0.46 / -0.47 | both halves | 3e-05 |  |
| [[PRMT3]] | -0.52 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[METTL8]] | -0.52 | -0.56 / -0.51 | both halves | 1e-05 |  |
| [[DPH6]] | -0.52 | -0.52 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PPARA]] | C | PPARA's natural level weakens BAZ2A's drug response | PPARA's natural level across 47 lines (lineage-adjusted; a glimpse) | r -0.65, reverse +0.10; direction not clear | 0.057 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 074]]; 63 genes; every member is in the + arm (projection on the module's main direction 0.592). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-4.8, -43.9); signed map (-17.1, 6.6). **Vector** length 107, 31.2% of its response variance represented; |z| ≥ 3 in 889 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~36% of this change | +4.7 | +5.2 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.4 | +1.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.9 | +1.2 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +3.3 | +6.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | +3.2 | -2.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.8 | +0.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.8 | -1.3 |
|  | [[Entrectinib (drug)]] 5 µM |  | +2.8 | +0.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.7 | +0.3 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +2.5 | -0.1 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -8.2 | -7.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.6 | -6.3 |
|  | [[EX229 (drug)]] 5 µM |  | -4.0 | -2.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -4.0 | -2.2 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~7% of this change | -3.8 | +4.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.6 | -3.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | -3.5 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | bromodomain adjacent to zinc finger domain 2A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.3 — chr12:56,595,596-56,636,816 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0314, TIP5, WALp3 |
| Gene groups (HGNC) | PHD finger proteins; Methyl-CpG binding domain containing; Bromodomain containing; NoRC complex |
| Hallmark sets | ADIPOGENESIS |
| Reactome | 3 pathways, smallest: NoRC negatively regulates rRNA expression; Negative epigenetic regulation of rRNA expression; Epigenetic regulation of gene expression |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UIF9](https://www.uniprot.org/uniprotkb/Q9UIF9) (Bromodomain adjacent to zinc finger domain protein 2A):

> Regulatory subunit of the ATP-dependent NoRC-1 and NoRC-5 ISWI chromatin remodeling complexes, which form ordered nucleosome arrays on chromatin and facilitate access to DNA during DNA-templated processes such as DNA replication, transcription, and repair. Both complexes regulate the spacing of nucleosomes along the chromatin and have the ability to slide mononucleosomes to the center of a DNA template. Directly stimulates the ATPase activity of SMARCA5 in the NoRC-5 ISWI chromatin remodeling …

**Summary**, from NCBI Gene [11176](https://www.ncbi.nlm.nih.gov/gene/11176):

> Enables histone binding activity. Contributes to RNA polymerase I core promoter sequence-specific DNA binding activity. Predicted to be involved in DNA methylation-dependent constitutive heterochromatin formation; negative regulation of transcription by RNA polymerase I; and rDNA heterochromatin formation. Predicted to act upstream of or within heterochromatin formation. Located in nuclear speck. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:962](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:962) · Entrez [11176](https://www.ncbi.nlm.nih.gov/gene/11176) · UniProt [Q9UIF9](https://www.uniprot.org/uniprotkb/Q9UIF9) · Ensembl [ENSG00000076108](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000076108)

## Data

Gene col 1144: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1144); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1144, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1144]; `tensor/DDL_lfc|DDL_z.npy` [1144]; `embed/gene_vectors.npy` [1144]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1144 or target_col == 1144). Every well: [[BAZ2A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BAZ2A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
