---
symbol: "GSPT2"
type: "gene"
col: 12121
ensembl_id: "ENSG00000189369"
name: "G1 to S phase transition 2"
location: "Xp11.22"
module: 11
arm: "+"
pooled_cpm: 6.01
n_lines_expressing: 36
n_dd_up: 8
n_dd_down: 3
n_dd_up_clean: 6
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 2
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# GSPT2

*G1 to S phase transition 2* — Xp11.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 2.46× (z +9.2, q 1e-17, up in 28 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.562× (z -8.3, q 4e-14, down in 24 of 29 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 4 lines (PANC-1 0.147×, SNU-423 0.0733×, MIA PaCa-2 0.158×, RPMI-7951 0.137×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (SW1417 0.239×, RKO 0.209×, Panc 03.27 0.186×); [[Niclosamide (olamine) (drug)]] 5 µM in 2 lines (NCI-H460 0.149×, A-427 0.129×; ⚠ toxic); [[Digitoxin (drug)]] 0.5 µM in 1 line (NCI-H460 0.0939×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (NCI-H460 0.167×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MRFAP1L1]] (+0.84, fdr 7e-06), [[ZNF155]] (+0.78, fdr 7e-06), [[KLHL9]] (+0.77, fdr 7e-06); moves opposite to [[NAP1L4]] (-0.71, fdr 7e-06), [[PIGN]] (-0.67, fdr 1e-05), [[SETD3]] (-0.66, fdr 1e-05).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 2 go from it, the strongest it → [[RPA1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12121.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **2.46×** | +9.2 | 1e-17 | 28/32 (HEC-1-A, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.47×** | +9.0 | 1e-16 | 26/32 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.34×** | +8.7 | 4e-16 | 24/29 (PANC-1, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.76×** | +8.2 | 3e-14 | 21/33 (HEC-1-A, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.58×** | +6.6 | 4e-09 | 19/33 (PANC-1, A-172, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.86×** | +6.1 | 8e-08 | 14/25 (SW1417, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.70×** | +5.4 | 4e-06 | 20/31 (A549, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.60×** | +4.9 | 8e-05 | 17/31 (AsPC-1, NCI-H2347, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.11× | +3.9 | 0.006 | 0/33 | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~54% of this change | 1.35× | +3.1 | 0.12 | 7/23 (A-172, SNU-423, …) | inconsistent across doses | low cells (technical?); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12121.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 4 lines (PANC-1 0.147×, SNU-423 0.0733×, MIA PaCa-2 0.158×, RPMI-7951 0.137×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (SW1417 0.239×, RKO 0.209×, Panc 03.27 0.186×); [[Niclosamide (olamine) (drug)]] 5 µM in 2 lines (NCI-H460 0.149×, A-427 0.129×; ⚠ toxic); [[Digitoxin (drug)]] 0.5 µM in 1 line (NCI-H460 0.0939×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (NCI-H460 0.167×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.562×** | -8.3 | 4e-14 | 24/29 (SW1417, RKO, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.643×** | -4.5 | 0.002 | 14/21 (PANC-1, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.692×** | -3.6 | 0.056 | 13/31 (A-427, LS 180, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Folic acid (drug)]] 5 µM |  | 0.792× | -3.4 | 0.11 | 11/33 (PANC-1, HOP62, …) | top dose only | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | 0.730× | -3.1 | 0.22 | 11/29 (NCI-H2347, NCI-H2030, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.742× | -3.0 | 0.22 | 8/31 (NCI-H460, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, +0.41 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12121. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 9.26 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0939× (z -14.4) |
| [[A-427 (line)]] | wt | 11.8 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.129× (z -10.8) ⚠ toxic · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.163× (z -9.6) |
| [[Hs 766T (line)]] | wt | 6.84 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0555× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Lidocaine (hydrochloride) (drug)]] 0.5 µM 0.111× (z -8.7) |
| [[HEC-1-A (line)]] | alt | 11.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.176× (z -9.6) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 9.89 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.156× (z -8.7) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 15.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.158× (z -10.4) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 8.26 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.186× (z -10.2) |
| [[PANC-1 (line)]] | alt | 11.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.147× (z -13.0) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 11.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.209× (z -10.3) |
| [[RPMI-7951 (line)]] | alt | 12.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.137× (z -8.8) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 12.5 | 0 | 1 | — | [[Decitabine (drug)]] 0.5 µM 0.0690× (z -10.4) |
| [[SNU-423 (line)]] | alt | 9.95 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0733× (z -11.4) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 18.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.239× (z -12.2) |
| [[A-172 (line)]] | wt | 5.98 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.430 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 5.68 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.958 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 4.30 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.454 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.548 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.79 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.17 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.459 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.539 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 4.56 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.599 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.03 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.444 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.469 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.474 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.25 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.457 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.419 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 3.77 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.06 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.81 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.88 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.79 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.44 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.79 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.48 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.99 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.555 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.433 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12121), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRFAP1L1]] | +0.84 | +0.77 / +0.86 | both halves | 7e-06 |  |
| [[ZNF155]] | +0.78 | +0.74 / +0.77 | both halves | 7e-06 |  |
| [[KLHL9]] | +0.77 | +0.67 / +0.80 | both halves | 7e-06 |  |
| [[PDRG1]] | +0.75 | +0.72 / +0.78 | both halves | 7e-06 |  |
| [[PHAX]] | +0.73 | +0.66 / +0.73 | both halves | 7e-06 |  |
| [[METTL18]] | +0.73 | +0.76 / +0.73 | both halves | 7e-06 |  |
| [[MSL3P1]] | +0.73 | +0.64 / +0.81 | both halves | 7e-06 |  |
| [[ERCC4]] | +0.72 | +0.74 / +0.69 | both halves | 7e-06 |  |
| [[RPP25L]] | +0.72 | +0.71 / +0.69 | both halves | 7e-06 |  |
| [[EID2]] | +0.72 | +0.71 / +0.69 | both halves | 7e-06 |  |
| [[UTP3]] | +0.72 | +0.75 / +0.72 | both halves | 7e-06 |  |
| [[NSMCE3]] | +0.72 | +0.66 / +0.72 | both halves | 7e-06 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NAP1L4]] | -0.71 | -0.65 / -0.73 | both halves | 7e-06 |  |
| [[PIGN]] | -0.67 | -0.54 / -0.71 | both halves | 1e-05 |  |
| [[SETD3]] | -0.66 | -0.56 / -0.70 | both halves | 1e-05 |  |
| [[RPA1]] | -0.62 | -0.60 / -0.64 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RPA1]] | B | GSPT2 activity raises RPA1's level | lines that do not express GSPT2 (14) vs lines expressing it (36) | 1.12× lower at baseline in the lines without GSPT2 | 0.049 | ⚠ within organs, on part of the lines; also absent: PALM2AKAP2, KCNN4, MDFIC |
| [[TMED4]] | B | GSPT2 activity raises TMED4's level | lines that do not express GSPT2 (14) vs lines expressing it (36) | 1.10× lower at baseline in the lines without GSPT2 | 0.084 | ⚠ within organs, on part of the lines; also absent: PALM2AKAP2, KCNN4, MDFIC |

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.802). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-34.0, 8.6); signed map (0.3, -23.0). **Vector** length 66.0, 14.1% of its response variance represented; |z| ≥ 3 in 609 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +5.2 | +9.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.1 | +9.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.6 | +8.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.3 | +5.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | +2.9 | +8.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.9 | +4.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.6 | +2.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.4 | +2.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.1 | +1.8 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -6.4 | -4.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -6.2 | -1.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -5.2 | -2.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.0 | -8.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -4.5 | -3.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.2 | -0.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.0 | -2.0 |
|  | [[Irinotecan (hydrochloride) (drug)]] 0.5 µM |  | -0.9 | -2.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -0.9 | +1.0 |
|  | [[Fumaric acid (drug)]] 0.5 µM |  | -0.8 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | G1 to S phase transition 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp11.22 — chrX:51,743,442-51,746,232 (+) |
| Ensembl biotype | protein_coding |
| Also known as | eRF3b, FLJ10441 |
| Gene groups (HGNC) | SURF complex; Translational GTPases |
| Reactome | 10 pathways, smallest: Eukaryotic Translation Termination; Nonsense Mediated Decay (NMD) independent of the Exon Junction Complex (EJC); Nonsense Mediated Decay (NMD) enhanced by the Exon Junction Complex (EJC) |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IYD1](https://www.uniprot.org/uniprotkb/Q8IYD1) (Eukaryotic peptide chain release factor GTP-binding subunit ERF3B):

> GTPase component of the eRF1-eRF3-GTP ternary complex, a ternary complex that mediates translation termination in response to the termination codons UAA, UAG and UGA. GSPT2/ERF3B mediates ETF1/ERF1 delivery to stop codons: The eRF1-eRF3-GTP complex binds to a stop codon in the ribosomal A-site. GTP hydrolysis by GSPT2/ERF3B induces a conformational change that leads to its dissociation, permitting ETF1/ERF1 to accommodate fully in the A-site. Component of the transient SURF complex which …

**Summary**, from NCBI Gene [23708](https://www.ncbi.nlm.nih.gov/gene/23708):

> This gene encodes a GTPase that belongs to the GTP-binding elongation factor family. The encoded protein is a polypeptide release factor that complexes with eukaryotic peptide chain release factor 1 to mediate translation termination. This protein may also be involved in mRNA stability.[provided by RefSeq, Mar 2010]

**Accessions** — [HGNC:4622](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4622) · Entrez [23708](https://www.ncbi.nlm.nih.gov/gene/23708) · UniProt [Q8IYD1](https://www.uniprot.org/uniprotkb/Q8IYD1) · Ensembl [ENSG00000189369](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000189369)

## Data

Gene col 12121: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12121); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12121, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12121]; `tensor/DDL_lfc|DDL_z.npy` [12121]; `embed/gene_vectors.npy` [12121]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12121 or target_col == 12121). Every well: [[GSPT2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GSPT2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
