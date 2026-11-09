---
symbol: "TCHP"
type: "gene"
col: 6307
ensembl_id: "ENSG00000139437"
name: "trichoplein keratin filament binding"
location: "12q24.11"
module: 1
arm: "+"
pooled_cpm: 20.14
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 2
n_dd_up_clean: 8
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# TCHP

*trichoplein keratin filament binding* — 12q24.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.22× (z +13.9, q 3e-41, up in 36 of 42 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 1.77× (z +9.9, q 6e-21, up in 34 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.736× (z -5.3, q 6e-05, down in 25 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 2 lines (NCI-H1573 0.139×, SNU-1 0.190×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SK-MEL-2 0.354×; ⚠ cell-cycle shift, explains ~24% of this change); [[Thymol (drug)]] 0.5 µM in 1 line (HCT15 0.115×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BAZ1B]] (+0.67, fdr 7e-06), [[DIS3L]] (+0.61, fdr 7e-06), [[DPH5]] (+0.60, fdr 1e-05); moves opposite to [[DPM1]] (-0.60, fdr 1e-05), [[SERF2]] (-0.57, fdr 1e-05), [[PIK3C2A]] (-0.57, fdr 2e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → [[ANKRD40]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6307.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.22×** | +13.9 | 3e-41 | 36/42 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.94×** | +11.1 | 4e-26 | 26/30 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.77×** | +9.9 | 6e-21 | 34/47 (NCI-H1792, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.81×** | +9.5 | 2e-19 | 27/37 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **1.73×** | +9.2 | 3e-18 | 35/47 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.44×** | +8.9 | 4e-17 | 27/47 (NCI-H1792, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.59×** | +8.1 | 5e-14 | 34/47 (SW480, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.46×** | +6.6 | 3e-09 | 23/48 (A549, SW480, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.34×** | +4.9 | 6e-05 | 18/44 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.21×** | +4.8 | 9e-05 | 18/48 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.28×** | +4.3 | 7e-04 | 18/48 (LoVo, SW1417, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~32% of this change | **1.29×** | +4.3 | 7e-04 | 16/45 (hTERT-HPNE, A549, …) | top dose only | position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **1.28×** | +4.2 | 0.001 | 18/47 (PANC-1, LS 180, …) | top dose only |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.36×** | +3.8 | 0.006 | 13/46 (MIA PaCa-2, HOP62, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.20×** | +3.2 | 0.050 | 16/47 (SW480, A549, …) | two highest doses |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 1.20× | +3.2 | 0.058 | 14/47 (NCI-H460, LOX-IMVI, …) | all doses, flat | position effect removed |
| [[Filgotinib (drug)]] 5 µM |  | 1.19× | +3.0 | 0.082 | 3/48 (C32, HS-578T, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6307.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 2 lines (NCI-H1573 0.139×, SNU-1 0.190×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SK-MEL-2 0.354×; ⚠ cell-cycle shift, explains ~24% of this change); [[Thymol (drug)]] 0.5 µM in 1 line (HCT15 0.115×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.736×** | -5.3 | 6e-05 | 25/48 (AsPC-1, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.769×** | -4.6 | 0.001 | 21/46 (NCI-H1573, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Anethole trithione (drug)]] 0.5 µM |  | 0.827× | -3.3 | 0.17 | 4/48 (SW480, RKO, …) | two highest doses | position effect removed |
| [[Irinotecan (hydrochloride) (drug)]] 0.5 µM |  | 0.832× | -3.2 | 0.17 | 2/48 (A498, J82) | inconsistent across doses | position effect removed |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 0.878× | -3.2 | 0.17 | 11/48 (NCI-H2347, Hs 766T, …) | rises with dose | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.836× | -3.1 | 0.17 | 13/47 (NCI-H1573, J82, …) | rises with dose |  |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | 0.779× | -3.1 | 0.17 | 3/48 (SW480, SK-MEL-2, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[TAK-733 (drug)]] 0.05 µM |  | 0.831× | -3.0 | 0.18 | 5/48 (CFPAC-1, A-172, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6307. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 21.3 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +10.0) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[NCI-H1792 (line)]] | alt | 13.0 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.6× (z +18.4) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.08× (z +8.9) | — |
| [[HCT15 (line)]] | alt | 15.6 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.115× (z -9.2) |
| [[hTERT-HPNE (line)]] | wt | 14.1 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.81× (z +8.9) ⚠ cell-cycle shift, explains ~24% of this change | — |
| [[LS 180 (line)]] | wt | 16.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.27× (z +8.7) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 17.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.45× (z +8.9) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 19.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.139× (z -13.9) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 33.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.62× (z +8.6) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 22.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.83× (z +10.3) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 23.6 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.354× (z -9.2) ⚠ cell-cycle shift, explains ~24% of this change |
| [[SNU-1 (line)]] | wt | 28.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.190× (z -8.9) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 17.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.42× (z +10.7) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 18.7 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 25.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 18.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 18.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 30.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.63 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 25.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 19.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 28.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 22.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 22.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6307), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BAZ1B]] | +0.67 | +0.74 / +0.62 | both halves | 7e-06 |  |
| [[DIS3L]] | +0.61 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[DPH5]] | +0.60 | +0.67 / +0.51 | both halves | 1e-05 |  |
| [[NOP14]] | +0.59 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[CPSF2]] | +0.58 | +0.66 / +0.54 | both halves | 1e-05 |  |
| [[ANAPC7]] | +0.58 | +0.58 / +0.58 | both halves | 8e-06 |  |
| [[THOC7]] | +0.58 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[ERCC4]] | +0.57 | +0.71 / +0.48 | both halves | 2e-05 |  |
| [[TCERG1]] | +0.56 | +0.58 / +0.43 | both halves | 4e-05 |  |
| [[DPP8]] | +0.56 | +0.61 / +0.47 | both halves | 2e-05 |  |
| [[CEP41]] | +0.56 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[RANGAP1]] | +0.56 | +0.51 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*37 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DPM1]] | -0.60 | -0.56 / -0.58 | both halves | 1e-05 |  |
| [[SERF2]] | -0.57 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[PIK3C2A]] | -0.57 | -0.65 / -0.47 | both halves | 2e-05 |  |
| [[TOR1B]] | -0.56 | -0.57 / -0.44 | both halves | 3e-05 |  |
| [[TMED4]] | -0.56 | -0.60 / -0.55 | both halves | 1e-05 |  |
| [[P4HA1]] | -0.56 | -0.62 / -0.47 | both halves | 2e-05 |  |
| [[OST4]] | -0.55 | -0.61 / -0.45 | both halves | 3e-05 |  |
| [[SSR4]] | -0.54 | -0.60 / -0.40 | both halves | 5e-05 |  |
| [[GUK1]] | -0.54 | -0.57 / -0.50 | both halves | 1e-05 |  |
| [[FUCA1]] | -0.54 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[SRP54-AS1]] | -0.54 | -0.56 / -0.43 | both halves | 3e-05 |  |
| [[TBC1D22A-DT]] | -0.54 | -0.53 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ANKRD40]] | C | TCHP's natural level weakens ANKRD40's drug response | TCHP's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.64, reverse +0.13; direction not clear | 0.061 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.526). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-14.2, -28.5); signed map (10.3, -35.3). **Vector** length 82.9, 16.0% of its response variance represented; |z| ≥ 3 in 866 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.5 | +13.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.4 | +11.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.2 | +6.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.2 | +9.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.7 | +8.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.1 | +1.8 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +2.4 | +3.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.4 | +4.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.3 | +1.3 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | -2.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.6 | -5.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.3 | -4.6 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | -1.5 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -1.8 | -3.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.7 | -1.0 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.6 | -2.7 |
|  | [[EX229 (drug)]] 0.05 µM |  | -1.3 | -1.8 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.2 | -1.8 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | -1.2 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | trichoplein keratin filament binding |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.11 — chr12:109,900,264-109,983,841 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC10854, TpMs |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BT92](https://www.uniprot.org/uniprotkb/Q9BT92) (Trichoplein keratin filament-binding protein):

> Tumor suppressor which has the ability to inhibit cell growth and be pro-apoptotic during cell stress. Inhibits cell growth in bladder and prostate cancer cells by a down-regulation of HSPB1 by inhibiting its phosphorylation. May act as a 'capping' or 'branching' protein for keratin filaments in the cell periphery. May regulate K8/K18 filament and desmosome organization mainly at the apical or peripheral regions of simple epithelial cells. Is a negative regulator of ciliogenesis.

**Summary**, from NCBI Gene [84260](https://www.ncbi.nlm.nih.gov/gene/84260):

> Involved in apoptotic process; negative regulation of cell growth; and negative regulation of cilium assembly. Located in several cellular components, including apical cortex; cytoskeleton; and mitochondrion. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:28135](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28135) · Entrez [84260](https://www.ncbi.nlm.nih.gov/gene/84260) · UniProt [Q9BT92](https://www.uniprot.org/uniprotkb/Q9BT92) · Ensembl [ENSG00000139437](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000139437)

## Data

Gene col 6307: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6307); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6307, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6307]; `tensor/DDL_lfc|DDL_z.npy` [6307]; `embed/gene_vectors.npy` [6307]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6307 or target_col == 6307). Every well: [[TCHP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TCHP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
