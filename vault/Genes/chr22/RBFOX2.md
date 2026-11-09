---
symbol: "RBFOX2"
type: "gene"
col: 1925
ensembl_id: "ENSG00000100320"
name: "RNA binding fox-1 homolog 2"
location: "22q12.3"
module: 149
arm: "+"
pooled_cpm: 269.78
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 6
n_dd_up_clean: 0
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/149"]
generated_by: "tahoemap"
---

# RBFOX2

*RNA binding fox-1 homolog 2* — 22q12.3

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 6 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (NCI-H23 1.87×, A-427 1.73×, A498 1.49×; ⚠ cell-cycle shift, explains ~77% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 3 lines (A498 1.72×, A-427 1.78×, MIA PaCa-2 1.63×; ⚠ cell-cycle shift, explains ~0% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (SW480 1.64×; ⚠ cell-cycle shift, explains ~0% of this change); [[TAK-901 (drug)]] 0.05 µM in 1 line (C32 1.98×); [[Ponatinib (drug)]] 5 µM in 1 line (C32 1.84×); [[PH-797804 (drug)]] 5 µM in 1 line (SW48 3.72×).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 0.663× (z -13.0, q 1e-35, down in 37 of 47 measured lines) ⚠ toxic. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.784× (z -11.0, q 2e-25, down in 28 of 49 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EPB41L2]] (+0.55, fdr 1e-05), [[CNN3]] (+0.53, fdr 3e-05), [[WWC2]] (+0.52, fdr 3e-05); moves opposite to [[NFKBIL1]] (-0.52, fdr 1e-05), [[ZBTB49]] (-0.51, fdr 4e-05), [[ZNF766]] (-0.51, fdr 3e-05).
> It is in [[Module 149]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CDH2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 4 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1925.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 6 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (NCI-H23 1.87×, A-427 1.73×, A498 1.49×; ⚠ cell-cycle shift, explains ~77% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 3 lines (A498 1.72×, A-427 1.78×, MIA PaCa-2 1.63×; ⚠ cell-cycle shift, explains ~0% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (SW480 1.64×; ⚠ cell-cycle shift, explains ~0% of this change); [[TAK-901 (drug)]] 0.05 µM in 1 line (C32 1.98×); [[Ponatinib (drug)]] 5 µM in 1 line (C32 1.84×); [[PH-797804 (drug)]] 5 µM in 1 line (SW48 3.72×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +4.9 | 5e-04 | 20/48 (SW480, SW1417, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.14× | +4.3 | 0.004 | 16/48 (SW480, C32, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.12× | +3.7 | 0.045 | 10/48 (SW480, NCI-H460, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.11× | +3.3 | 0.12 | 9/48 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Verteporfin (drug)]] 5 µM |  | 1.10× | +3.1 | 0.21 | 4/49 (NCI-H2030, SW 900, …) | top dose only |  |
| [[Tadalafil (drug)]] 5 µM |  | 1.10× | +3.1 | 0.21 | 2/48 (A498, BT-474) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 9 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1925.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.663×** | -13.0 | 1e-35 | 37/47 (NCI-H2347, RKO, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.784×** | -11.0 | 2e-25 | 28/49 (HS-578T, PANC-1, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.719×** | -10.8 | 5e-25 | 40/48 (SW480, HEC-1-A, …) | two highest doses | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.788×** | -7.8 | 8e-13 | 30/48 (HEC-1-A, SW480, …) | two highest doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~13% of this change | **0.817×** | -6.6 | 4e-09 | 29/48 (HOP62, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | 0.837× | -5.6 | 2e-06 | 22/48 (C32, LoVo, …) | rises with dose | composition shift |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.773×** | -5.2 | 1e-05 | 35/47 (AsPC-1, NCI-H23, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | 0.879× | -3.9 | 0.006 | 19/45 (SW480, RKO, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change | 0.888× | -3.9 | 0.006 | 18/49 (RKO, NCI-H2347, …) | all doses, flat | composition shift |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | 0.920× | -3.7 | 0.011 | 0/48 | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | 0.901× | -3.4 | 0.033 | 13/48 (SW480, RKO, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.903× | -3.3 | 0.040 | 9/48 (NCI-H2347, HS-578T, …) | inconsistent across doses |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 0.904× | -3.3 | 0.042 | 2/48 (A549, hTERT-HPNE) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.902× | -3.2 | 0.048 | 13/48 (BT-474, C32, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change | 0.904× | -3.2 | 0.057 | 16/44 (NCI-H23, C-33 A, …) | all doses, flat | composition shift |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | 0.908× | -3.1 | 0.078 | 6/49 (H4, J82, …) | rises with dose |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | 0.912× | -3.0 | 0.080 | 9/48 (Hs 766T, NCI-H460, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.05 µM |  | 0.907× | -3.0 | 0.097 | 6/48 (BT-474, LoVo, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1925. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 450 | 2 | 5 (4 ⚠) | [[TAK-901 (drug)]] 0.05 µM 1.98× (z +10.7) | [[Harringtonine (drug)]] 0.5 µM 0.418× (z -14.4) ⚠ cell-cycle shift, explains ~17% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.654× (z -9.6) |
| [[NCI-H2347 (line)]] | alt | 258 | 0 | 6 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.491× (z -13.3) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.619× (z -12.8) |
| [[RKO (line)]] | wt | 423 | 0 | 5 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.468× (z -13.3) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.514× (z -12.1) |
| [[NCI-H1573 (line)]] | alt | 259 | 0 | 4 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.462× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 271 | 1 (1 ⚠) | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.64× (z +11.9) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 0.5 µM 0.537× (z -15.2) |
| [[A-427 (line)]] | wt | 164 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.73× (z +12.5) ⚠ cell-cycle shift, explains ~77% of this change | — |
| [[HS-578T (line)]] | alt | 471 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.542× (z -15.8) |
| [[C-33 A (line)]] | alt | 382 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.454× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change |
| [[HEC-1-A (line)]] | alt | 294 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.570× (z -12.3) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.571× (z -12.3) |
| [[HOP62 (line)]] | alt | 294 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.623× (z -8.8) ⚠ toxic |
| [[LoVo (line)]] | wt | 269 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.606× (z -9.7) ⚠ cell-cycle shift, explains ~17% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.640× (z -8.9) |
| [[MIA PaCa-2 (line)]] | alt | 299 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 1.63× (z +8.9) ⚠ cell-cycle shift, explains ~0% of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.560× (z -10.3) ⚠ toxic |
| [[NCI-H23 (line)]] | alt | 300 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.87× (z +15.3) ⚠ cell-cycle shift, explains ~77% of this change | [[Dinaciclib (drug)]] 5 µM 0.458× (z -13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change |
| [[SW48 (line)]] | wt | 268 | 1 | 1 | [[PH-797804 (drug)]] 5 µM 3.72× (z +8.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.587× (z -9.7) |
| [[A498 (line)]] | wt | 280 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 1.72× (z +11.5) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[A549 (line)]] | wt | 207 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.633× (z -8.5) |
| [[BT-474 (line)]] | alt | 204 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.658× (z -8.8) |
| [[CFPAC-1 (line)]] | alt | 261 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.592× (z -8.8) ⚠ toxic |
| [[CHP-212 (line)]] | wt | 341 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.371× (z -9.9) |
| [[H4 (line)]] | wt | 259 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.523× (z -8.6) ⚠ cell-cycle shift, explains ~17% of this change |
| [[hTERT-HPNE (line)]] | wt | 375 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.546× (z -8.5) ⚠ toxic |
| [[KATO III (line)]] | alt | 307 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.487× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change |
| [[LS 180 (line)]] | wt | 254 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.607× (z -9.5) |
| [[Panc 03.27 (line)]] | alt | 276 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.599× (z -9.0) |
| [[PANC-1 (line)]] | alt | 250 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 1.53× (z +9.8) ⚠ toxic; cell-cycle shift, explains ~0% of this change | — |
| [[SHP-77 (line)]] | alt | 276 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.605× (z -11.5) |
| [[SK-MEL-2 (line)]] | alt | 120 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.485× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change |
| [[SW 1088 (line)]] | alt | 404 | 0 | 1 | — | [[Naproxen (drug)]] 0.05 µM 0.246× (z -8.7) |
| [[SW1417 (line)]] | alt | 172 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.587× (z -9.4) ⚠ toxic |
| [[A-172 (line)]] | wt | 188 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 310 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 245 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 215 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 388 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 178 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 392 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 183 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 210 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 311 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 282 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 293 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 268 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 208 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 276 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 218 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 275 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 283 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 279 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 278 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 236 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1925), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*34 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EPB41L2]] | +0.55 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[CNN3]] | +0.53 | +0.43 / +0.52 | both halves | 3e-05 |  |
| [[WWC2]] | +0.52 | +0.48 / +0.44 | both halves | 3e-05 |  |
| [[CORO1C]] | +0.51 | +0.49 / +0.62 | both halves | 1e-05 |  |
| [[PKM]] | +0.51 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[DPY19L1]] | +0.50 | +0.50 / +0.46 | both halves | 2e-05 |  |
| [[CDH2]] | +0.49 | +0.31 / +0.38 | both halves | 2e-04 |  |
| [[MAN1A2]] | +0.48 | +0.46 / +0.40 | both halves | 5e-05 |  |
| [[SPCS3]] | +0.48 | +0.51 / +0.42 | both halves | 4e-05 |  |
| [[CAV2]] | +0.48 | +0.52 / +0.38 | both halves | 7e-05 |  |
| [[VOPP1]] | +0.47 | +0.45 / +0.41 | both halves | 4e-05 |  |
| [[ASPH]] | +0.46 | +0.40 / +0.49 | both halves | 4e-05 |  |

## Genes that move opposite

*66 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NFKBIL1]] | -0.52 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[ZBTB49]] | -0.51 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[ZNF766]] | -0.51 | -0.43 / -0.52 | both halves | 3e-05 |  |
| [[MTERF4]] | -0.50 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[ZNF333]] | -0.50 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[BRAP]] | -0.50 | -0.51 / -0.44 | both halves | 3e-05 |  |
| [[HEIH]] | -0.48 | -0.34 / -0.55 | both halves | 1e-04 |  |
| [[ZNF449]] | -0.48 | -0.25 / -0.45 | both halves | 4e-04 |  |
| [[ZSCAN32]] | -0.47 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[CIAO3]] | -0.47 | -0.40 / -0.44 | both halves | 4e-05 |  |
| [[SETDB1]] | -0.47 | -0.49 / -0.55 | both halves | 1e-05 |  |
| [[ZNF7]] | -0.47 | -0.38 / -0.41 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CDH2]] | B | CDH2 activity raises RBFOX2's level | lines that do not express CDH2 (22) vs lines expressing it (28) | 1.11× lower at baseline in the lines without CDH2 | 0.062 | ⚠ within organs, on part of the lines; also absent: ARMCX1, DKK3, RFTN1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 149]]; 30 genes; every member is in the + arm (projection on the module's main direction -0.482). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.41; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-35.2, 0.7); signed map (-14.8, 31.4). **Vector** length 91.9, 23.0% of its response variance represented; |z| ≥ 3 in 1,009 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.4 | -0.6 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.4 | +0.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.3 | +0.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.2 | +4.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.8 | +2.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.2 | +3.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.0 | +0.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +1.6 | +1.9 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -5.9 | -13.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.0 | -11.0 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~13% of this change | -3.8 | -6.6 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.9 | -1.5 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -2.7 | -2.0 |
|  | [[Budesonide (drug)]] 0.5 µM |  | -2.6 | -2.7 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | -2.5 | -3.0 |
|  | [[Budesonide (drug)]] 0.05 µM |  | -2.4 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | RNA binding fox-1 homolog 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q12.3 — chr22:35,738,736-36,028,824 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HNRBP2, FOX-2, HRNBP2; previously RBM9 |
| Gene groups (HGNC) | RNA binding motif containing; RNA binding fox-1 homologs |
| Reactome | 4 pathways, smallest: FGFR2 alternative splicing; Signaling by FGFR2; Signaling by FGFR |
| Matched by | ensembl_id |

**Function**, from UniProt [O43251](https://www.uniprot.org/uniprotkb/O43251) (RNA binding protein fox-1 homolog 2):

> RNA-binding protein that regulates alternative splicing events by binding to 5'-UGCAUGU-3' elements. Prevents binding of U2AF2 to the 3'-splice site. Regulates alternative splicing of tissue-specific exons and of differentially spliced exons during erythropoiesis (By similarity). RNA-binding protein that seems to act as a coregulatory factor of ER-alpha. Together with RNA binding proteins RBPMS and MBNL1/2, activates vascular smooth muscle cells alternative splicing events.

**Summary**, from NCBI Gene [23543](https://www.ncbi.nlm.nih.gov/gene/23543):

> This gene is one of several human genes similar to the C. elegans gene Fox-1. This gene encodes an RNA binding protein that is thought to be a key regulator of alternative exon splicing in the nervous system and other cell types. The protein binds to a conserved UGCAUG element found downstream of many alternatively spliced exons and promotes inclusion of the alternative exon in mature transcripts. The protein also interacts with the estrogen receptor 1 transcription factor and regulates …

**Accessions** — [HGNC:9906](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9906) · Entrez [23543](https://www.ncbi.nlm.nih.gov/gene/23543) · UniProt [O43251](https://www.uniprot.org/uniprotkb/O43251) · Ensembl [ENSG00000100320](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100320)

## Data

Gene col 1925: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1925); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1925, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1925]; `tensor/DDL_lfc|DDL_z.npy` [1925]; `embed/gene_vectors.npy` [1925]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1925 or target_col == 1925). Every well: [[RBFOX2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RBFOX2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
