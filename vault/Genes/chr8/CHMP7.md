---
symbol: "CHMP7"
type: "gene"
col: 7186
ensembl_id: "ENSG00000147457"
name: "charged multivesicular body protein 7"
location: "8p21.3"
module: 16
arm: "+"
pooled_cpm: 19.6
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 3
n_dd_up_clean: 6
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# CHMP7

*charged multivesicular body protein 7* — 8p21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 1.49× (z +5.9, q 3e-06, up in 32 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 0.691× (z -5.1, q 2e-04, down in 18 of 35 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Anethole trithione (drug)]] 5 µM: 0.800× (z -4.7, q 7e-04, down in 26 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 7 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 4 lines (NCI-H1573 0.115×, HCT15 0.141×, HS-578T 0.323×, AsPC-1 0.293×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (LoVo 0.192×, LS 180 0.180×, HCT15 0.215×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (MIA PaCa-2 0.167×, HS-578T 0.242×; ⚠ cell-cycle shift, explains ~0% of this change); [[Ipatasertib (drug)]] 0.5 µM in 1 line (RPMI-7951 0.0817×); [[Radotinib (drug)]] 0.5 µM in 1 line (RPMI-7951 0.193×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TXLNA]] (+0.67, fdr 7e-06), [[DNAJC14]] (+0.64, fdr 7e-06), [[CANT1]] (+0.63, fdr 1e-05); moves opposite to [[PNISR]] (-0.57, fdr 1e-05), [[MROH8]] (-0.54, fdr 2e-05), [[FLJ40194]] (-0.52, fdr 5e-05).
> It sits in the **+** arm of [[Module 016]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7186.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **1.49×** | +5.9 | 3e-06 | 32/48 (CFPAC-1, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~25% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.39×** | +4.9 | 3e-04 | 20/45 (SW 900, HOP62, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~13% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.24×** | +4.5 | 0.001 | 16/48 (SW480, NCI-H2030, …) | top dose only | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.09× | +4.3 | 0.002 | 0/48 | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.33×** | +4.2 | 0.003 | 16/47 (MIA PaCa-2, SW480, …) | two highest doses | cell-cycle shift (explains ~16% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **1.57×** | +3.5 | 0.043 | 12/48 (SW480, LS 180, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.28×** | +3.4 | 0.062 | 11/46 (NCI-H2030, HOP62, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[PF-06260933 (drug)]] 5 µM |  | **1.52×** | +3.3 | 0.078 | 7/45 (NCI-H2030, LoVo, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | 1.24× | +3.1 | 0.11 | 10/48 (LS 180, SW480, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 5 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7186.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 7 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 4 lines (NCI-H1573 0.115×, HCT15 0.141×, HS-578T 0.323×, AsPC-1 0.293×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (LoVo 0.192×, LS 180 0.180×, HCT15 0.215×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (MIA PaCa-2 0.167×, HS-578T 0.242×; ⚠ cell-cycle shift, explains ~0% of this change); [[Ipatasertib (drug)]] 0.5 µM in 1 line (RPMI-7951 0.0817×); [[Radotinib (drug)]] 0.5 µM in 1 line (RPMI-7951 0.193×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.691×** | -5.1 | 2e-04 | 18/35 (SW480, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Anethole trithione (drug)]] 5 µM |  | **0.800×** | -4.7 | 7e-04 | 26/48 (SW 900, SW480, …) | top dose only | cell-cycle shift (explains ~5% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.735×** | -4.6 | 8e-04 | 23/42 (NCI-H1573, HCT15, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.855× | -3.3 | 0.13 | 19/47 (HS-578T, SW 900, …) | top dose only | position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.858× | -3.3 | 0.13 | 18/47 (hTERT-HPNE, NCI-H2030, …) | top dose only | composition shift |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.860× | -3.1 | 0.19 | 10/48 (C-33 A, NCI-H2030, …) | inconsistent across doses |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.816× | -3.0 | 0.19 | 8/48 (SW 1088, NCI-H23, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7186. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 30.7 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.242× (z -11.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 32.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.141× (z -11.6) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 19.9 | 0 | 2 | — | [[Ipatasertib (drug)]] 0.5 µM 0.0817× (z -9.3) |
| [[AN3 CA (line)]] | alt | 30.3 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.104× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 27.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.293× (z -8.6) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 20.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.192× (z -14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 24.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.180× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 21.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.167× (z -12.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 19.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.115× (z -14.2) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 22.6 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.258× (z -8.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 21.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.200× (z -13.7) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 21.8 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 23.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 23.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 23.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.82 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 21.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 24.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 22.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.79 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 17.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 44.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 9.00 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 32.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 25.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.14 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.16 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 21.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7186), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TXLNA]] | +0.67 | +0.65 / +0.65 | both halves | 7e-06 |  |
| [[DNAJC14]] | +0.64 | +0.58 / +0.58 | both halves | 7e-06 |  |
| [[CANT1]] | +0.63 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[TINF2]] | +0.60 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[ZNF445]] | +0.60 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[PANK4]] | +0.59 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[C15orf39]] | +0.58 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[PUF60]] | +0.58 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[TUBG1]] | +0.57 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[ZKSCAN2]] | +0.57 | +0.40 / +0.62 | both halves | 5e-05 |  |
| [[ZFP62]] | +0.56 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[RIC8A]] | +0.56 | +0.59 / +0.44 | both halves | 3e-05 | STRING 530 |

## Genes that move opposite

*18 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PNISR]] | -0.57 | -0.57 / -0.51 | both halves | 1e-05 |  |
| [[MROH8]] | -0.54 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[FLJ40194]] | -0.52 | -0.53 / -0.40 | both halves | 5e-05 |  |
| [[PABPN1]] | -0.52 | -0.51 / -0.43 | both halves | 3e-05 |  |
| [[EOGT-DT]] | -0.51 | -0.46 / -0.42 | both halves | 4e-05 |  |
| [[ZBTB47-AS1]] | -0.51 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[VAMP2]] | -0.50 | -0.55 / -0.38 | both halves | 6e-05 |  |
| [[HSPA2-AS1]] | -0.50 | -0.45 / -0.40 | both halves | 5e-05 |  |
| [[ELF2]] | -0.50 | -0.41 / -0.50 | both halves | 4e-05 |  |
| [[CRNDE]] | -0.49 | -0.49 / -0.42 | both halves | 4e-05 |  |
| [[KPNB1-DT]] | -0.49 | -0.54 / -0.41 | both halves | 4e-05 |  |
| [[NAA38]] | -0.48 | -0.47 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers CHMP7's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **+** arm (projection on the module's main direction 0.343). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-30.2, -11.7); signed map (-14.7, -28.9). **Vector** length 75.4, 12.9% of its response variance represented; |z| ≥ 3 in 801 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +4.6 | +4.9 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | +3.5 | +3.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +3.0 | +4.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.9 | +4.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.9 | +5.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.8 | +3.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.7 | +2.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.2 | +2.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.8 | +1.9 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.9 | -3.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -3.2 | -5.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -3.0 | -4.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.7 | -2.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.6 | -1.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.9 | -1.9 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | -1.9 | -3.1 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -1.6 | -0.1 |
|  | [[Bergenin (drug)]] 0.5 µM |  | -1.6 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | charged multivesicular body protein 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p21.3 — chr8:23,243,637-23,262,000 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC29816 |
| Gene groups (HGNC) | Charged multivesicular body proteins; ESCRT-III associated factors |
| Reactome | 29 pathways, smallest: Translation of Replicase and Assembly of the Replication Transcription Complex_9679504; Translation of Replicase and Assembly of the Replication Transcription Complex_9694676; Pyroptosis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WUX9](https://www.uniprot.org/uniprotkb/Q8WUX9) (Charged multivesicular body protein 7):

> ESCRT-III-like protein required to recruit the ESCRT-III complex to the nuclear envelope (NE) during late anaphase. Together with SPAST, the ESCRT-III complex promotes NE sealing and mitotic spindle disassembly during late anaphase. Recruited to the reforming NE during anaphase by LEMD2. Plays a role in the endosomal sorting pathway.

**Summary**, from NCBI Gene [91782](https://www.ncbi.nlm.nih.gov/gene/91782):

> Involved in several processes, including midbody abscission; mitotic nuclear division; and vacuolar transport. Located in several cellular components, including bounding membrane of organelle; chromosome; and nucleus. Part of ESCRT III complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:28439](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28439) · Entrez [91782](https://www.ncbi.nlm.nih.gov/gene/91782) · UniProt [Q8WUX9](https://www.uniprot.org/uniprotkb/Q8WUX9) · Ensembl [ENSG00000147457](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000147457)

## Data

Gene col 7186: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7186); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7186, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7186]; `tensor/DDL_lfc|DDL_z.npy` [7186]; `embed/gene_vectors.npy` [7186]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7186 or target_col == 7186). Every well: [[CHMP7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CHMP7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
