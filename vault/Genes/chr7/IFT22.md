---
symbol: "IFT22"
type: "gene"
col: 4896
ensembl_id: "ENSG00000128581"
name: "intraflagellar transport 22"
location: "7q22.1"
module: 17
arm: "+"
pooled_cpm: 8.36
n_lines_expressing: 49
n_dd_up: 25
n_dd_down: 0
n_dd_up_clean: 15
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# IFT22

*intraflagellar transport 22* — 7q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.46× (z +11.4, q 1e-27, up in 29 of 32 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 3.44× (z +11.4, q 1e-27, up in 45 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idoxuridine (drug)]] 0.05 µM in 1 line (AN3 CA 0.0670×); [[Cepharanthine (drug)]] 5 µM in 1 line (Hs 766T 0.184×); [[Imiquimod (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H2030 0.117×; ⚠ toxic).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NPHP1]] (+0.77, fdr 7e-06), [[ASB8]] (+0.71, fdr 7e-06), [[DCTN3]] (+0.70, fdr 7e-06); moves opposite to [[GART]] (-0.59, fdr 1e-05), [[RCC1]] (-0.57, fdr 3e-04), [[KLHL29]] (-0.54, fdr 3e-05).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[GIHCG]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 10 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4896.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **3.46×** | +11.4 | 1e-27 | 29/32 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.44×** | +11.4 | 1e-27 | 45/47 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **3.35×** | +11.1 | 2e-26 | 44/47 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **3.07×** | +10.0 | 3e-21 | 17/17 (SW480, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM |  | **2.78×** | +9.4 | 4e-19 | 44/46 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.64×** | +6.4 | 1e-08 | 28/44 (SW480, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **2.01×** | +6.2 | 5e-08 | 29/45 (SW480, C-33 A, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **2.04×** | +6.1 | 8e-08 | 15/22 (HEC-1-A, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.93×** | +5.8 | 3e-07 | 26/36 (SW1417, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.85×** | +5.7 | 8e-07 | 29/41 (SW480, SW48, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.67×** | +4.7 | 1e-04 | 27/47 (SK-MEL-2, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~46% of this change | **1.57×** | +4.2 | 0.001 | 17/37 (NCI-H2030, Hs 766T, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.49×** | +3.7 | 0.010 | 17/46 (C-33 A, HEC-1-A, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.30×** | +3.4 | 0.027 | 16/47 (RKO, Panc 03.27, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.44×** | +3.3 | 0.032 | 14/42 (NCI-H2030, NCI-H661, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.40×** | +3.1 | 0.069 | 8/46 (SW480, A498, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **1.89×** | +3.1 | 0.069 | 10/46 (A498, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 5 µM |  | **1.40×** | +3.0 | 0.078 | 9/47 (LoVo, LS 180, …) | top dose only |  |
| [[Amsacrine (drug)]] 5 µM |  | **1.26×** | +3.0 | 0.078 | 11/47 (SW480, A-427, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.38×** | +3.0 | 0.078 | 12/47 (KATO III, LoVo, …) | rises with dose | position effect removed |
| [[Arbutin (drug)]] 5 µM |  | **1.40×** | +2.9 | 0.082 | 5/45 (NCI-H460, A549, …) | top dose only | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.37×** | +2.9 | 0.087 | 11/47 (LoVo, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Sulfatinib (drug)]] 5 µM |  | **1.39×** | +2.9 | 0.090 | 7/46 (SW48, NCI-H23, …) | top dose only |  |
| [[Entrectinib (drug)]] 5 µM |  | **1.36×** | +2.9 | 0.096 | 7/46 (KATO III, A498, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4896.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idoxuridine (drug)]] 0.05 µM in 1 line (AN3 CA 0.0670×); [[Cepharanthine (drug)]] 5 µM in 1 line (Hs 766T 0.184×); [[Imiquimod (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H2030 0.117×; ⚠ toxic).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 0.5 µM |  | 0.691× | -3.4 | 0.27 | 15/44 (HCT15, C32, …) | two highest doses | cell-cycle shift (explains ~21% here) |
| [[Hydroxyurea (drug)]] 5 µM |  | 0.695× | -3.2 | 0.27 | 15/46 (Panc 03.27, HOP62, …) | top dose only | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.708× | -3.2 | 0.27 | 15/46 (PANC-1, MIA PaCa-2, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.36 per unit of S-phase module lfc, +0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4896. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 10.4 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.17× (z +10.5) ⚠ cell-cycle shift, explains ~55% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 4.61× (z +9.8) | — |
| [[A-172 (line)]] | wt | 19.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.58× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[AN3 CA (line)]] | alt | 24.2 | 0 | 1 | — | [[Idoxuridine (drug)]] 0.05 µM 0.0670× (z -9.2) |
| [[Hs 766T (line)]] | wt | 6.18 | 0 | 1 | — | [[Cepharanthine (drug)]] 5 µM 0.184× (z -8.7) |
| [[LoVo (line)]] | wt | 7.50 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.11× (z +9.2) ⚠ cell-cycle shift, explains ~55% of this change | — |
| [[NCI-H2030 (line)]] | alt | 5.84 | 0 | 1 (1 ⚠) | — | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.117× (z -8.5) ⚠ toxic |
| [[NCI-H460 (line)]] | wt | 7.87 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.29× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[A-427 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.84 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 7.52 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.47 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.46 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.07 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.92 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.83 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.08 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 9.65 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.65 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.94 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.45 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.13 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.59 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.38 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.95 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.04 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.67 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.02 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.54 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.81 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.58 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 7.59 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.87 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.22 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.27 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.77 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.42 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.96 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.77 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.39 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.46 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.79 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4896), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 4 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NPHP1]] | +0.77 | +0.75 / +0.68 | both halves | 7e-06 | pathway: Assembly of the 9+0 primary cilium |
| [[ASB8]] | +0.71 | +0.71 / +0.67 | both halves | 7e-06 |  |
| [[DCTN3]] | +0.70 | +0.59 / +0.66 | both halves | 7e-06 | pathway: Assembly of the 9+0 primary cilium |
| [[BAD]] | +0.70 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[DNAAF4]] | +0.68 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[MORN2]] | +0.66 | +0.74 / +0.67 | both halves | 7e-06 |  |
| [[DNAL4]] | +0.63 | +0.57 / +0.69 | both halves | 1e-05 |  |
| [[TMEM254]] | +0.62 | +0.58 / +0.62 | both halves | 8e-06 |  |
| [[ATG4D]] | +0.60 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[NUDT16L1]] | +0.60 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[ENKD1]] | +0.58 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[IK]] | +0.58 | +0.55 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GART]] | -0.59 | -0.59 / -0.57 | both halves | 1e-05 |  |
| [[RCC1]] | -0.57 | -0.27 / -0.46 | both halves | 3e-04 |  |
| [[KLHL29]] | -0.54 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[MRPS25]] | -0.53 | -0.43 / -0.43 | both halves | 3e-05 |  |
| [[SEH1L]] | -0.53 | -0.68 / -0.49 | both halves | 1e-05 |  |
| [[BEND3]] | -0.52 | -0.43 / -0.42 | both halves | 4e-05 |  |
| [[PHKA1]] | -0.52 | -0.57 / -0.38 | both halves | 6e-05 |  |
| [[TRNT1]] | -0.52 | -0.47 / -0.38 | both halves | 6e-05 |  |
| [[CYP27B1]] | -0.51 | -0.34 / -0.48 | both halves | 1e-04 |  |
| [[MAN2C1]] | -0.51 | -0.53 / -0.46 | both halves | 2e-05 |  |
| [[ABCC4]] | -0.50 | -0.43 / -0.52 | both halves | 3e-05 |  |
| [[TBC1D4]] | -0.49 | -0.52 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GIHCG]] | B | GIHCG activity raises IFT22's level | lines that do not express GIHCG (9) vs lines expressing it (41) | 1.55× lower at baseline in the lines without GIHCG | 0.010 | ⚠ within organs, on part of the lines; also absent: BOLA3-DT, LIX1L, HLTF; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.519). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-25.8, 0.1); signed map (-10.8, -2.4). **Vector** length 64.6, 11.9% of its response variance represented; |z| ≥ 3 in 801 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +3.3 | +2.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | +3.1 | +6.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.0 | +11.4 |
|  | [[Belinostat (drug)]] 5 µM |  | +2.9 | +9.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | +2.8 | +11.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.0 | +3.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.9 | +3.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.5 | +0.5 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +1.4 | +2.5 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.4 | +1.1 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -4.3 | -2.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.8 | -3.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -3.7 | -3.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.2 | +1.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.2 | +1.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -1.7 | -0.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.7 | +0.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.6 | -0.2 |
|  | [[EX229 (drug)]] 5 µM |  | -1.5 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | intraflagellar transport 22 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q22.1 — chr7:101,310,914-101,321,823 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ14117, FLJ13225, DKFZp761N0823, FAP9, CFAP9; previously RABL5 |
| Gene groups (HGNC) | RAB like GTPases; IFT-B1 complex |
| Reactome | 4 pathways, smallest: Intraflagellar transport; Assembly of the 9+0 primary cilium; Cilium Assembly |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H7X7](https://www.uniprot.org/uniprotkb/Q9H7X7) (Intraflagellar transport protein 22 homolog):

> Small GTPase-like component of the intraflagellar transport (IFT) complex B.

**Summary**, from NCBI Gene [64792](https://www.ncbi.nlm.nih.gov/gene/64792):

> Predicted to enable GTPase activity. Predicted to be involved in intracellular protein transport. Part of intraciliary transport particle A. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:21895](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21895) · Entrez [64792](https://www.ncbi.nlm.nih.gov/gene/64792) · UniProt [Q9H7X7](https://www.uniprot.org/uniprotkb/Q9H7X7) · Ensembl [ENSG00000128581](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000128581)

## Data

Gene col 4896: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4896); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4896, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4896]; `tensor/DDL_lfc|DDL_z.npy` [4896]; `embed/gene_vectors.npy` [4896]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4896 or target_col == 4896). Every well: [[IFT22 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IFT22.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
