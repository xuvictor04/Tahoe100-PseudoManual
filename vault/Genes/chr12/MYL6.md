---
symbol: "MYL6"
type: "gene"
col: 1708
ensembl_id: "ENSG00000092841"
name: "myosin light chain 6"
location: "12q13.2"
module: 33
arm: "-"
pooled_cpm: 167.95
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 0
n_dd_up_clean: 7
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/033"]
generated_by: "tahoemap"
---

# MYL6

*myosin light chain 6* — 12q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.90× (z +10.7, q 7e-24, up in 46 of 49 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.54× (z +5.4, q 4e-06, up in 38 of 49 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Apalutamide (drug)]] 0.05 µM in 1 line (SW 1088 0.0748×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATP6V0C]] (+0.56, fdr 2e-05), [[CTNND1]] (+0.52, fdr 1e-05), [[ITSN1]] (+0.52, fdr 3e-05); moves opposite to [[DDX31]] (-0.58, fdr 1e-05), [[GSTO2]] (-0.56, fdr 2e-05), [[NLE1]] (-0.55, fdr 1e-05).
> It sits in the **-** arm of [[Module 033]] (MYC targets v2).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 11 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1708.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **2.90×** | +10.7 | 7e-24 | 46/49 (PANC-1, J82, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.33×** | +10.2 | 3e-22 | 47/50 (AsPC-1, J82, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **2.68×** | +10.1 | 1e-21 | 43/44 (PANC-1, SNU-423, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **1.83×** | +6.5 | 1e-08 | 44/48 (PANC-1, NCI-H460, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **1.92×** | +6.4 | 1e-08 | 37/45 (J82, SNU-423, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.68×** | +5.6 | 3e-06 | 41/48 (PANC-1, NCI-H460, …) | rises with dose | composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.54×** | +5.4 | 4e-06 | 38/49 (SNU-423, A549, …) | top dose only | cell-cycle shift (explains ~9% here); noisy plate (z scaled); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~43% of this change | **1.58×** | +4.9 | 7e-05 | 42/48 (SW 900, SW 1271, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.44×** | +3.9 | 0.005 | 29/48 (NCI-H460, PANC-1, …) | rises with dose | position effect removed |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.44×** | +3.6 | 0.015 | 37/47 (LS 180, COLO 205, …) | all doses, flat |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.78×** | +3.4 | 0.031 | 35/48 (LS 180, LoVo, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.37×** | +3.3 | 0.036 | 26/48 (SW480, Panc 03.27, …) | two highest doses |  |
| [[Peretinoin (drug)]] 0.05 µM |  | **1.40×** | +3.3 | 0.036 | 33/48 (BT-474, HT-29, …) | all doses, flat |  |
| [[vincristine (drug)]] 5 µM |  | **1.78×** | +3.2 | 0.050 | 31/46 (HT-29, LS 180, …) | rises with dose | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.35×** | +3.2 | 0.050 | 27/48 (NCI-H460, PANC-1, …) | rises with dose | position effect removed |
| [[Mifepristone (drug)]] 0.05 µM |  | **1.36×** | +3.0 | 0.079 | 31/47 (A498, AsPC-1, …) | inconsistent across doses | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.33×** | +3.0 | 0.080 | 28/48 (LS 180, NCI-H1573, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1708.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Apalutamide (drug)]] 0.05 µM in 1 line (SW 1088 0.0748×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | 0.550× | -3.3 | 0.53 | 26/48 (SNU-1, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.748× | -3.1 | 0.58 | 38/49 (SW1417, Panc 03.27, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, +0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1708. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 102 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.51× (z +13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[SNU-423 (line)]] | alt | 156 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.09× (z +12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.67× (z +8.6) | — |
| [[J82 (line)]] | alt | 209 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.43× (z +13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 110 | 3 (3 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 1.51× (z +10.7) ⚠ position not correctable | — |
| [[NCI-H460 (line)]] | wt | 126 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.31× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[A498 (line)]] | wt | 147 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.92× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[A549 (line)]] | wt | 140 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.72× (z +12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[HEC-1-A (line)]] | alt | 209 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.89× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[HOP62 (line)]] | alt | 144 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.16× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[HS-578T (line)]] | alt | 175 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.54× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[KATO III (line)]] | alt | 147 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.17× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[NCI-H1792 (line)]] | alt | 87.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.32× (z +11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[NCI-H23 (line)]] | alt | 177 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.09× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[RPMI-7951 (line)]] | alt | 167 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.35× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[SW 900 (line)]] | alt | 156 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.99× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[A-427 (line)]] | wt | 274 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.37× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[C-33 A (line)]] | alt | 111 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.86× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[C32 (line)]] | wt | 88.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.54× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[Hs 766T (line)]] | wt | 133 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.22× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 213 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.51× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[LoVo (line)]] | wt | 178 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.69× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[NCI-H1573 (line)]] | alt | 167 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.71× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[Panc 03.27 (line)]] | alt | 244 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.08× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[SHP-77 (line)]] | alt | 69.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.84× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 81.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.93× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[SW 1088 (line)]] | alt | 187 | 0 | 1 | — | [[Apalutamide (drug)]] 0.05 µM 0.0748× (z -11.8) |
| [[SW480 (line)]] | alt | 129 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.82× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[A-172 (line)]] | wt | 188 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 134 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 316 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 223 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 304 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 129 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 155 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 188 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 169 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 169 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 141 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 184 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 203 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 157 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 298 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 161 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 208 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 198 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 199 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 139 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 139 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 132 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1708), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*26 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP6V0C]] | +0.56 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[CTNND1]] | +0.52 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[ITSN1]] | +0.52 | +0.44 / +0.50 | both halves | 3e-05 | pathway: EPH-Ephrin signaling |
| [[TP53INP2]] | +0.51 | +0.48 / +0.51 | both halves | 2e-05 |  |
| [[RTL8C]] | +0.51 | +0.44 / +0.54 | both halves | 3e-05 |  |
| [[CDKL5]] | +0.49 | +0.41 / +0.59 | both halves | 4e-05 |  |
| [[PPDPF]] | +0.49 | +0.43 / +0.51 | both halves | 3e-05 |  |
| [[CAVIN1]] | +0.49 | +0.47 / +0.46 | both halves | 3e-05 |  |
| [[PTMS]] | +0.48 | +0.47 / +0.49 | both halves | 2e-05 |  |
| [[FKBP3]] | +0.48 | +0.36 / +0.58 | both halves | 1e-04 |  |
| [[RAB5B]] | +0.48 | +0.37 / +0.55 | both halves | 8e-05 |  |
| [[HLA-A]] | +0.48 | +0.49 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*74 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DDX31]] | -0.58 | -0.59 / -0.50 | both halves | 1e-05 |  |
| [[GSTO2]] | -0.56 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[NLE1]] | -0.55 | -0.52 / -0.57 | both halves | 1e-05 |  |
| [[EIF3M]] | -0.53 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[TSEN2]] | -0.53 | -0.46 / -0.59 | both halves | 3e-05 |  |
| [[NUDT19]] | -0.53 | -0.57 / -0.38 | both halves | 6e-05 |  |
| [[SNHG17]] | -0.53 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[RAD51D]] | -0.53 | -0.49 / -0.46 | both halves | 3e-05 |  |
| [[ZNF485]] | -0.52 | -0.49 / -0.44 | both halves | 3e-05 |  |
| [[UBA2]] | -0.52 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[POLR1B]] | -0.52 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[HMBS]] | -0.52 | -0.47 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 033]] — MYC targets v2; 139 genes; this gene is in the **-** arm (projection on the module's main direction -0.554). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-11.0, -46.5); signed map (-14.4, 18.9). **Vector** length 97.2, 36.9% of its response variance represented; |z| ≥ 3 in 776 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | +6.2 | +5.6 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | +4.8 | +6.5 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~60% of this change | +4.7 | +3.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | +4.6 | +3.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.8 | +2.0 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.4 | +2.3 |
|  | [[RMC-6236 (drug)]] 5 µM |  | +3.0 | -0.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.0 | +1.5 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +2.9 | +1.2 |
| fall | [[Auranofin (drug)]] 5 µM |  | -4.0 | +0.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.1 | -3.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.9 | -0.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.9 | -0.3 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.8 | -0.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.2 | +0.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -1.9 | +0.3 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -1.9 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | myosin light chain 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.2 — chr12:56,158,346-56,163,496 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ESMLC, MLC3NM, MLC1SM |
| Gene groups (HGNC) | Myosin light chains, class 1 |
| Reactome | 16 pathways, smallest: RHO GTPases Activate ROCKs; RHO GTPases activate CIT; Sema4D induced cell migration and growth-cone collapse |
| Matched by | ensembl_id |

**Function**, from UniProt [P60660](https://www.uniprot.org/uniprotkb/P60660) (Myosin light polypeptide 6):

> Regulatory light chain of myosin. Does not bind calcium.

**Summary**, from NCBI Gene [4637](https://www.ncbi.nlm.nih.gov/gene/4637):

> Myosin is a hexameric ATPase cellular motor protein. It is composed of two heavy chains, two nonphosphorylatable alkali light chains, and two phosphorylatable regulatory light chains. This gene encodes a myosin alkali light chain that is expressed in smooth muscle and non-muscle tissues. Genomic sequences representing several pseudogenes have been described and two transcript variants encoding different isoforms have been identified for this gene. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:7587](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7587) · Entrez [4637](https://www.ncbi.nlm.nih.gov/gene/4637) · UniProt [P60660](https://www.uniprot.org/uniprotkb/P60660) · Ensembl [ENSG00000092841](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000092841)

## Data

Gene col 1708: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1708); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1708, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1708]; `tensor/DDL_lfc|DDL_z.npy` [1708]; `embed/gene_vectors.npy` [1708]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1708 or target_col == 1708). Every well: [[MYL6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MYL6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
