---
symbol: "PDP2"
type: "gene"
col: 10305
ensembl_id: "ENSG00000172840"
name: "pyruvate dehydrogenase phosphatase catalytic subunit 2"
location: "16q22.1"
module: 3
arm: "+"
pooled_cpm: 17.59
n_lines_expressing: 49
n_dd_up: 24
n_dd_down: 3
n_dd_up_clean: 19
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# PDP2

*pyruvate dehydrogenase phosphatase catalytic subunit 2* — 16q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.14× (z +13.7, q 6e-40, up in 43 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 0.432× (z -7.9, q 2e-12, down in 28 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (J82 0.0977×, A498 0.290×, A-172 0.206×; ⚠ toxic; transcription drop); [[Hesperidin (drug)]] 5 µM in 1 line (AN3 CA 0.0831×); [[Lidocaine (hydrochloride) (drug)]] 0.5 µM in 1 line (CHP-212 0.0939×); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (SNU-1 0.126×).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GGT7]] (+0.60, fdr 1e-05), [[MAP2K7]] (+0.59, fdr 1e-05), [[BCAT2]] (+0.56, fdr 3e-05); moves opposite to [[EIF4G2]] (-0.57, fdr 1e-04), [[XRCC6]] (-0.55, fdr 3e-05), [[COPS3]] (-0.52, fdr 5e-05).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → [[LAMTOR5]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10305.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **2.14×** | +13.7 | 6e-40 | 43/47 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.03×** | +12.7 | 2e-34 | 42/47 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.85×** | +11.0 | 5e-26 | 40/46 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.66×** | +9.1 | 1e-17 | 36/46 (NCI-H460, NCI-H2030, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.48×** | +7.1 | 2e-10 | 29/47 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Berbamine (drug)]] 5 µM |  | **1.27×** | +6.0 | 2e-07 | 21/47 (NCI-H2030, LS 180, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.38×** | +5.8 | 5e-07 | 23/46 (SW480, SNU-423, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.26×** | +5.8 | 5e-07 | 24/46 (A-172, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **1.84×** | +5.8 | 5e-07 | 21/47 (SW480, SK-MEL-2, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.33×** | +5.0 | 4e-05 | 17/44 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.30×** | +4.8 | 1e-04 | 17/46 (SW480, NCI-H460, …) | inconsistent across doses |  |
| [[Cepharanthine (drug)]] 5 µM |  | 1.20× | +4.6 | 2e-04 | 22/47 (NCI-H2030, A498, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.42×** | +4.5 | 3e-04 | 15/45 (NCI-H1573, RPMI-7951, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.28×** | +4.4 | 4e-04 | 12/46 (C32, KATO III, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.24×** | +3.9 | 0.003 | 11/47 (NCI-H1792, A549, …) | top dose only |  |
| [[venetoclax (drug)]] 5 µM |  | **1.51×** | +3.9 | 0.004 | 11/43 (SW480, RPMI-7951, …) | top dose only | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.34×** | +3.8 | 0.005 | 9/47 (NCI-H460, LoVo, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10305.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (J82 0.0977×, A498 0.290×, A-172 0.206×; ⚠ toxic; transcription drop); [[Hesperidin (drug)]] 5 µM in 1 line (AN3 CA 0.0831×); [[Lidocaine (hydrochloride) (drug)]] 0.5 µM in 1 line (CHP-212 0.0939×); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (SNU-1 0.126×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.432×** | -7.9 | 2e-12 | 28/47 (NCI-H460, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.572×** | -5.3 | 4e-05 | 19/46 (NCI-H23, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.787×** | -4.2 | 0.006 | 14/29 (J82, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | 0.830× | -3.4 | 0.11 | 17/40 (MIA PaCa-2, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | 0.831× | -3.1 | 0.23 | 12/36 (Panc 03.27, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, -0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10305. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 17.3 | 3 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 8.57× (z +18.0) | [[Dinaciclib (drug)]] 5 µM 0.206× (z -9.1) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 27.8 | 4 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.27× (z +11.8) ⚠ cell-cycle shift, explains ~20% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 2.62× (z +9.8) | — |
| [[A-427 (line)]] | wt | 16.2 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.265× (z -8.5) ⚠ cell-cycle shift, explains ~20% of this change |
| [[A498 (line)]] | wt | 21.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.290× (z -10.0) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 36.3 | 0 | 1 | — | [[Hesperidin (drug)]] 5 µM 0.0831× (z -10.9) |
| [[CHP-212 (line)]] | wt | 48.1 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.5 µM 0.0939× (z -10.9) |
| [[HEC-1-A (line)]] | alt | 13.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.09× (z +10.2) | — |
| [[J82 (line)]] | alt | 13.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0977× (z -13.9) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 30.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.330× (z -8.5) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 27.4 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.56× (z +9.1) | — |
| [[SNU-1 (line)]] | wt | 20.9 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.126× (z -9.6) |
| [[SNU-423 (line)]] | alt | 16.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +9.2) | — |
| [[A549 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.64 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.63 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.99 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.79 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 31.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 17.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10305), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 6 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GGT7]] | +0.60 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[MAP2K7]] | +0.59 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[BCAT2]] | +0.56 | +0.45 / +0.59 | both halves | 3e-05 |  |
| [[PGPEP1]] | +0.56 | +0.37 / +0.52 | both halves | 8e-05 |  |
| [[DOCK6]] | +0.55 | +0.35 / +0.50 | both halves | 1e-04 |  |
| [[MCRIP2]] | +0.55 | +0.39 / +0.51 | both halves | 6e-05 |  |
| [[MVD]] | +0.54 | +0.49 / +0.44 | both halves | 3e-05 |  |
| [[BRI3]] | +0.53 | +0.36 / +0.56 | both halves | 9e-05 |  |
| [[SQLE]] | +0.53 | +0.37 / +0.51 | both halves | 8e-05 |  |
| [[RSAD1]] | +0.53 | +0.34 / +0.55 | both halves | 1e-04 |  |
| [[SPATA2L]] | +0.53 | +0.40 / +0.49 | both halves | 5e-05 |  |
| [[NSUN5P1-1]] | +0.53 | +0.37 / +0.59 | both halves | 8e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIF4G2]] | -0.57 | -0.35 / -0.60 | both halves | 1e-04 |  |
| [[XRCC6]] | -0.55 | -0.45 / -0.57 | both halves | 3e-05 |  |
| [[COPS3]] | -0.52 | -0.40 / -0.56 | both halves | 5e-05 |  |
| [[C5]] | -0.51 | -0.31 / -0.35 | both halves | 2e-04 |  |
| [[DR1]] | -0.51 | -0.34 / -0.52 | both halves | 1e-04 |  |
| [[ATL3]] | -0.51 | -0.31 / -0.55 | both halves | 2e-04 |  |
| [[POGLUT3]] | -0.51 | -0.35 / -0.51 | both halves | 1e-04 |  |
| [[YWHAE]] | -0.50 | -0.37 / -0.52 | both halves | 8e-05 |  |
| [[XNDC1N]] | -0.50 | -0.41 / -0.37 | both halves | 9e-05 |  |
| [[PSME3IP1]] | -0.50 | -0.20 / -0.52 | both halves | 7e-04 |  |
| [[VBP1]] | -0.50 | -0.34 / -0.46 | both halves | 1e-04 |  |
| [[MOB1A]] | -0.49 | -0.29 / -0.53 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LAMTOR5]] | C | PDP2's natural level weakens LAMTOR5's drug response | PDP2's natural level across 47 lines (lineage-adjusted; a glimpse) | r -0.64, reverse -0.00; direction not clear | 0.071 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.508). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-35.1, -22.9); signed map (-25.7, 14.0). **Vector** length 84.0, 16.1% of its response variance represented; |z| ≥ 3 in 882 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +4.5 | +9.1 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +3.3 | +4.6 |
|  | [[Berbamine (drug)]] 5 µM |  | +2.6 | +6.0 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.6 | +4.4 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +2.6 | +5.8 |
|  | [[Almonertinib (mesylate) (drug)]] 5 µM |  | +2.4 | +3.3 |
| fall | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -5.0 | -2.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | -4.9 | -7.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.6 | -3.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.5 | -2.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -4.5 | -3.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.9 | -0.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.7 | -5.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.9 | -1.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.5 | -1.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.4 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | pyruvate dehydrogenase phosphatase catalytic subunit 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q22.1 — chr16:66,878,589-66,895,754 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1348, PPM2C2, PPM2B |
| Gene groups (HGNC) | Protein phosphatases, Mg2+/Mn2+ dependent |
| Reactome | 4 pathways, smallest: Regulation of pyruvate dehydrogenase (PDH) complex; Regulation of pyruvate metabolism; Pyruvate metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P2J9](https://www.uniprot.org/uniprotkb/Q9P2J9) ([Pyruvate dehydrogenase [acetyl-transferring]]-phosphatase 2, mitochondrial):

> Mitochondrial enzyme that catalyzes the dephosphorylation and concomitant reactivation of the alpha subunit of the E1 component of the pyruvate dehydrogenase complex (PDC), thereby stimulating the conversion of pyruvate into acetyl-CoA (By similarity). Acts as a crucial regulator of T cell metabolism and function, with a particular focus on T-helper Th17 (By similarity).

**Summary**, from NCBI Gene [57546](https://www.ncbi.nlm.nih.gov/gene/57546):

> This gene is a mitochondrial protein that functions as a phosphatase and is involved in the enzymatic resetting of the pyruvate dehydrogenase complex. Alternative splicing results in multiple transcript variants encoding the same protein. [provided by RefSeq, Aug 2016]

**Accessions** — [HGNC:30263](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30263) · Entrez [57546](https://www.ncbi.nlm.nih.gov/gene/57546) · UniProt [Q9P2J9](https://www.uniprot.org/uniprotkb/Q9P2J9) · Ensembl [ENSG00000172840](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000172840)

## Data

Gene col 10305: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10305); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10305, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10305]; `tensor/DDL_lfc|DDL_z.npy` [10305]; `embed/gene_vectors.npy` [10305]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10305 or target_col == 10305). Every well: [[PDP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PDP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
