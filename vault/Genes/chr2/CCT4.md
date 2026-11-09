---
symbol: "CCT4"
type: "gene"
col: 3682
ensembl_id: "ENSG00000115484"
name: "chaperonin containing TCP1 subunit 4"
location: "2p15"
module: 60
arm: "+"
pooled_cpm: 162.39
n_lines_expressing: 50
n_dd_up: 28
n_dd_down: 0
n_dd_up_clean: 14
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/060"]
generated_by: "tahoemap"
---

# CCT4

*chaperonin containing TCP1 subunit 4* — 2p15

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (14 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 3.29× (z +16.5, q 0e+00, up in 48 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.403×; ⚠ cell-cycle shift, would explain all of this change); [[Harringtonine (drug)]] 5 µM in 1 line (A-427 0.440×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HSPD1]] (+0.85, fdr 7e-06), [[CCT3]] (+0.84, fdr 7e-06), [[HSP90AB1]] (+0.79, fdr 7e-06); moves opposite to [[YY1AP1]] (-0.67, fdr 7e-06), [[TNRC6C]] (-0.60, fdr 1e-05), [[TYK2]] (-0.58, fdr 1e-05).
> It sits in the **+** arm of [[Module 060]] (heat shock).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[DGKG]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 16 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3682.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **3.29×** | +16.5 | 0e+00 | 48/48 (C32, HT-29, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.31×** | +11.6 | 9e-29 | 48/48 (A-172, A498, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **2.31×** | +11.6 | 9e-29 | 49/49 (A549, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.29×** | +11.4 | 3e-28 | 47/48 (SW1417, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **2.33×** | +11.3 | 2e-27 | 42/44 (A549, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.10×** | +9.1 | 1e-17 | 46/48 (A498, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.85×** | +7.6 | 3e-12 | 44/45 (SW1417, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | **1.69×** | +7.0 | 2e-10 | 43/47 (COLO 205, NCI-H1792, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **1.61×** | +6.1 | 7e-08 | 38/45 (MIA PaCa-2, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **2.01×** | +5.1 | 2e-05 | 43/47 (PANC-1, A549, …) | inconsistent across doses | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.43×** | +4.9 | 4e-05 | 40/48 (NCI-H1792, HT-29, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.61×** | +4.7 | 1e-04 | 37/49 (SW1417, A498, …) | all doses, flat | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.40×** | +4.5 | 3e-04 | 35/47 (NCI-H2030, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.78×** | +4.2 | 0.001 | 37/48 (LOX-IMVI, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~73% of this change | **1.33×** | +3.9 | 0.003 | 30/48 (SW 900, CFPAC-1, …) | inconsistent across doses | low cells (technical?) |
| [[vincristine (drug)]] 0.5 µM |  | **1.42×** | +3.4 | 0.018 | 36/48 (HOP62, SK-MEL-2, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | **1.29×** | +3.4 | 0.022 | 29/48 (MIA PaCa-2, A549, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.56×** | +3.2 | 0.037 | 25/48 (KATO III, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.35×** | +3.0 | 0.072 | 24/47 (HT-29, C-33 A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Peretinoin (drug)]] 5 µM |  | **1.25×** | +2.9 | 0.078 | 27/47 (NCI-H460, MIA PaCa-2, …) | rises with dose |  |
| [[vincristine (drug)]] 5 µM |  | **1.48×** | +2.9 | 0.089 | 25/46 (HOP62, SK-MEL-2, …) | two highest doses | noisy plate (z scaled) |
| [[Infigratinib (drug)]] 5 µM |  | **1.48×** | +2.8 | 0.093 | 21/48 (AsPC-1, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[Sulfatinib (drug)]] 5 µM |  | **1.24×** | +2.8 | 0.093 | 20/49 (A549, A498, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3682.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 0.403×; ⚠ cell-cycle shift, would explain all of this change); [[Harringtonine (drug)]] 5 µM in 1 line (A-427 0.440×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | 0.760× | -3.4 | 0.30 | 31/50 (LoVo, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 0.838× | -3.3 | 0.30 | 18/48 (LoVo, SW480, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, +0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3682. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 208 | 7 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.02× (z +13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 2.86× (z +12.8) | — |
| [[A-172 (line)]] | wt | 123 | 6 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 4.65× (z +16.4) | — |
| [[HT-29 (line)]] | alt | 123 | 6 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 4.61× (z +17.2) | — |
| [[KATO III (line)]] | alt | 151 | 6 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.44× (z +14.3) | — |
| [[NCI-H1792 (line)]] | alt | 188 | 6 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.67× (z +12.8) ⚠ cell-cycle shift, would explain all of this change | — |
| [[CFPAC-1 (line)]] | alt | 89.3 | 5 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.22× (z +11.2) | — |
| [[HOP62 (line)]] | alt | 131 | 5 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 4.62× (z +15.9) | — |
| [[Hs 766T (line)]] | wt | 91.9 | 5 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 4.19× (z +12.1) | — |
| [[HS-578T (line)]] | alt | 97.0 | 5 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 4.09× (z +12.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 212 | 5 (3 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.68× (z +13.8) | — |
| [[RPMI-7951 (line)]] | alt | 130 | 5 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 4.35× (z +14.0) | — |
| [[SNU-423 (line)]] | alt | 112 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.37× (z +13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.78× (z +12.5) | — |
| [[SW1417 (line)]] | alt | 178 | 5 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.77× (z +13.1) | — |
| [[A-427 (line)]] | wt | 330 | 2 (1 ⚠) | 2 (2 ⚠) | [[Auranofin (drug)]] 5 µM 2.52× (z +11.0) | [[Homoharringtonine (drug)]] 5 µM 0.403× (z -15.4) ⚠ cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 175 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.53× (z +16.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 2.48× (z +9.1) | — |
| [[COLO 205 (line)]] | alt | 64.4 | 4 (2 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 6.73× (z +13.3) ⚠ toxic; cell-cycle shift, explains ~33% of this change · without an alert: [[Auranofin (drug)]] 5 µM 4.29× (z +10.5) | — |
| [[HEC-1-A (line)]] | alt | 139 | 4 | 0 | [[Auranofin (drug)]] 5 µM 4.17× (z +16.3) | — |
| [[LOX-IMVI (line)]] | wt | 202 | 4 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.79× (z +15.1) | — |
| [[NCI-H2347 (line)]] | alt | 128 | 4 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.55× (z +9.8) | — |
| [[Panc 03.27 (line)]] | alt | 120 | 4 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.58× (z +13.2) | — |
| [[PANC-1 (line)]] | alt | 198 | 4 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.93× (z +13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.53× (z +11.7) | — |
| [[RKO (line)]] | wt | 177 | 4 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.26× (z +14.1) | — |
| [[SW480 (line)]] | alt | 215 | 4 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.08× (z +13.1) | — |
| [[J82 (line)]] | alt | 104 | 3 | 0 | [[Auranofin (drug)]] 5 µM 2.49× (z +9.7) | — |
| [[NCI-H460 (line)]] | wt | 168 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.47× (z +13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.40× (z +9.8) | — |
| [[LoVo (line)]] | wt | 134 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 4.60× (z +15.9) | — |
| [[LS 180 (line)]] | wt | 137 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.41× (z +9.0) | — |
| [[NCI-H1573 (line)]] | alt | 120 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.88× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[NCI-H2030 (line)]] | alt | 234 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.16× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | — |
| [[SHP-77 (line)]] | alt | 157 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 2.47× (z +9.6) | — |
| [[SK-MEL-2 (line)]] | alt | 158 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.95× (z +14.3) | — |
| [[AN3 CA (line)]] | alt | 160 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.80× (z +9.8) | — |
| [[AsPC-1 (line)]] | alt | 134 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.30× (z +11.2) | — |
| [[BT-474 (line)]] | alt | 110 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.22× (z +13.1) | — |
| [[C-33 A (line)]] | alt | 187 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.23× (z +10.9) | — |
| [[C32 (line)]] | wt | 78.7 | 1 | 0 | [[Auranofin (drug)]] 5 µM 7.13× (z +17.2) | — |
| [[H4 (line)]] | wt | 112 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.71× (z +12.4) | — |
| [[HCT15 (line)]] | alt | 179 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.40× (z +10.9) | — |
| [[HepG2_C3A (line)]] | wt | 159 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.65× (z +9.7) | — |
| [[hTERT-HPNE (line)]] | wt | 105 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.28× (z +10.7) | — |
| [[NCI-H23 (line)]] | alt | 434 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.30× (z +9.9) | — |
| [[SNU-1 (line)]] | wt | 147 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.95× (z +12.8) | — |
| [[SW 900 (line)]] | alt | 123 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.57× (z +12.4) | — |
| [[CHP-212 (line)]] | wt | 149 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 138 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 191 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 133 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 229 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3682), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HSPD1]] | +0.85 | +0.83 / +0.82 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V1; STRING 623 |
| [[CCT3]] | +0.84 | +0.85 / +0.81 | both halves | 7e-06 | same gene group; pathway: HALLMARK_MYC_TARGETS_V1; STRING 999 |
| [[HSP90AB1]] | +0.79 | +0.77 / +0.78 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V1; STRING 946 |
| [[HSP90AA1]] | +0.79 | +0.74 / +0.79 | both halves | 7e-06 | pathway: Assembly of the 9+0 primary cilium; STRING 783 |
| [[CCT2]] | +0.77 | +0.80 / +0.74 | both halves | 7e-06 | same gene group; pathway: HALLMARK_MYC_TARGETS_V1; STRING 999 |
| [[CCT5]] | +0.76 | +0.84 / +0.68 | both halves | 7e-06 | same gene group; pathway: HALLMARK_MYC_TARGETS_V1; STRING 999 |
| [[CCT6A]] | +0.75 | +0.79 / +0.74 | both halves | 7e-06 | same gene group; pathway: Association of TriC/CCT with target proteins during biosynthesis; STRING 999 |
| [[TCP1]] | +0.75 | +0.79 / +0.71 | both halves | 7e-06 | same gene group; pathway: HALLMARK_MYC_TARGETS_V1; STRING 999 |
| [[HSP90AB3P]] | +0.74 | +0.73 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[HSP90AB2P]] | +0.73 | +0.71 / +0.67 | both halves | 7e-06 |  |
| [[HSPA8]] | +0.72 | +0.67 / +0.74 | both halves | 7e-06 | STRING 929 |
| [[CACYBP]] | +0.71 | +0.66 / +0.72 | both halves | 7e-06 | STRING 404 |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[YY1AP1]] | -0.67 | -0.59 / -0.68 | both halves | 7e-06 |  |
| [[TNRC6C]] | -0.60 | -0.62 / -0.52 | both halves | 1e-05 | pathway: Cilium Assembly |
| [[TYK2]] | -0.58 | -0.53 / -0.63 | both halves | 1e-05 |  |
| [[PHPT1]] | -0.57 | -0.67 / -0.49 | both halves | 1e-05 |  |
| [[SUSD6]] | -0.56 | -0.61 / -0.52 | both halves | 1e-05 |  |
| [[H2AJ]] | -0.56 | -0.42 / -0.54 | both halves | 4e-05 |  |
| [[ABCA5]] | -0.55 | -0.50 / -0.56 | both halves | 1e-05 |  |
| [[HLA-A]] | -0.55 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[REL]] | -0.54 | -0.48 / -0.53 | both halves | 2e-05 |  |
| [[PIK3IP1]] | -0.54 | -0.48 / -0.55 | both halves | 2e-05 |  |
| [[PLAG1]] | -0.53 | -0.58 / -0.53 | both halves | 1e-05 |  |
| [[CHKB]] | -0.52 | -0.47 / -0.49 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DGKG]] | B | DGKG activity lowers CCT4's level | lines that do not express DGKG (14) vs lines expressing it (36) | 1.34× higher at baseline in the lines without DGKG | 0.060 | ⚠ within organs, on part of the lines; also absent: CADPS2, RBPMS, SHC4; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 060]] — heat shock; 78 genes; this gene is in the **+** arm (projection on the module's main direction 0.815). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-19.8, -11.7); signed map (-26.3, -29.3). **Vector** length 97.8, 39.5% of its response variance represented; |z| ≥ 3 in 1,161 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *heat shock* (control, mean cos +0.54 to 13); *Attenuation phase* (reactome, mean cos +0.53 to 13); *HSF1-dependent transactivation* (reactome, mean cos +0.51 to 14).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +8.4 | +9.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +7.9 | +16.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +7.2 | +11.4 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +6.5 | +7.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +6.3 | +11.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.3 | +4.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.0 | +1.9 |
|  | [[EX229 (drug)]] 5 µM |  | +2.3 | +2.7 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -6.1 | +2.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.0 | -0.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -5.3 | -0.0 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.6 | +0.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.4 | +1.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.6 | -0.2 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | -2.0 | -0.2 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -1.9 | +0.2 |
|  | [[Thymol (drug)]] 0.5 µM |  | -1.8 | -0.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.8 | +0.6 |

## What is on record

|  |  |
|---|---|
| Name | chaperonin containing TCP1 subunit 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p15 — chr2:61,868,085-61,888,671 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Cctd |
| Gene groups (HGNC) | Chaperonin containing TCP1 |
| Hallmark sets | MYC_TARGETS_V1 |
| Reactome | 13 pathways, smallest: Folding of actin by CCT/TriC; Formation of tubulin folding intermediates by CCT/TriC; BBSome-mediated cargo-targeting to cilium |
| Matched by | ensembl_id |

**Function**, from UniProt [P50991](https://www.uniprot.org/uniprotkb/P50991) (T-complex protein 1 subunit delta):

> Component of the chaperonin-containing T-complex (TRiC), a molecular chaperone complex that assists the folding of actin, tubulin and other proteins upon ATP hydrolysis. The TRiC complex mediates the folding of WRAP53/TCAB1, thereby regulating telomere maintenance. As part of the TRiC complex may play a role in the assembly of BBSome, a complex involved in ciliogenesis regulating transports vesicles to the cilia.

**Summary**, from NCBI Gene [10575](https://www.ncbi.nlm.nih.gov/gene/10575):

> The chaperonin containing TCP1 (MIM 186980) complex (CCT), also called the TCP1 ring complex, consists of 2 back-to-back rings, each containing 8 unique but homologous subunits, such as CCT4. CCT assists the folding of newly translated polypeptide substrates through multiple rounds of ATP-driven release and rebinding of partially folded intermediate forms. Substrates of CCT include the cytoskeletal proteins actin (see MIM 102560) and tubulin (see MIM 191130), as well as alpha-transducin (MIM …

**Accessions** — [HGNC:1617](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1617) · Entrez [10575](https://www.ncbi.nlm.nih.gov/gene/10575) · UniProt [P50991](https://www.uniprot.org/uniprotkb/P50991) · Ensembl [ENSG00000115484](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000115484)

## Data

Gene col 3682: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3682); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3682, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3682]; `tensor/DDL_lfc|DDL_z.npy` [3682]; `embed/gene_vectors.npy` [3682]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3682 or target_col == 3682). Every well: [[CCT4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCT4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
