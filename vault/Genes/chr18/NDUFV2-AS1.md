---
symbol: "NDUFV2-AS1"
type: "gene"
col: 15477
ensembl_id: "ENSG00000266053"
name: "NDUFV2 antisense RNA 1"
location: "18p11.22"
module: 21
arm: "+"
pooled_cpm: 5.43
n_lines_expressing: 50
n_dd_up: 25
n_dd_down: 2
n_dd_up_clean: 22
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# NDUFV2-AS1

*NDUFV2 antisense RNA 1* — 18p11.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.16× (z +21.7, q 0e+00, up in 39 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.722× (z -4.3, q 0.005, down in 15 of 47 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Harringtonine (drug)]] 0.05 µM: 0.705× (z -4.3, q 0.005, down in 13 of 35 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Erlotinib (drug)]] 5 µM in 1 line (HS-578T 0.0540×); [[LJI308 (drug)]] 0.05 µM in 1 line (J82 0.0599×); [[Elagolix sodium (drug)]] 0.5 µM in 1 line (LOX-IMVI 0.0671×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HSPA2-AS1]] (+0.76, fdr 7e-06), [[CHMP3-AS1]] (+0.76, fdr 7e-06), [[UPK2]] (+0.76, fdr 7e-06); moves opposite to [[TCOF1]] (-0.69, fdr 7e-06), [[FBXW2]] (-0.63, fdr 3e-05), [[HERC2]] (-0.63, fdr 1e-05).
> It is in [[Module 021]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15477.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.16×** | +21.7 | 0e+00 | 39/40 (A-172, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.68×** | +18.6 | 0e+00 | 33/41 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.23×** | +10.7 | 2e-24 | 30/47 (HT-29, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.17×** | +10.3 | 8e-23 | 29/46 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.92×** | +8.7 | 3e-16 | 22/47 (HOP62, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.82×** | +7.7 | 1e-12 | 19/36 (HOP62, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.46×** | +7.2 | 5e-11 | 22/46 (SW1417, KATO III, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.43×** | +6.8 | 9e-10 | 18/46 (Panc 03.27, PANC-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.59×** | +6.2 | 4e-08 | 17/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.50×** | +5.5 | 3e-06 | 16/38 (A-172, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.50×** | +5.4 | 4e-06 | 12/44 (HOP62, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.42×** | +4.7 | 1e-04 | 8/46 (A-427, KATO III, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.42×** | +4.7 | 1e-04 | 9/28 (NCI-H1573, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.41×** | +4.6 | 1e-04 | 15/45 (RKO, HOP62, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.43×** | +4.6 | 2e-04 | 9/43 (A-427, A-172, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.27×** | +4.6 | 2e-04 | 12/48 (A-427, HEC-1-A, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15477.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Erlotinib (drug)]] 5 µM in 1 line (HS-578T 0.0540×); [[LJI308 (drug)]] 0.05 µM in 1 line (J82 0.0599×); [[Elagolix sodium (drug)]] 0.5 µM in 1 line (LOX-IMVI 0.0671×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.722×** | -4.3 | 0.005 | 15/47 (MIA PaCa-2, HOP62, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.705×** | -4.3 | 0.005 | 13/35 (SW1417, Hs 766T, …) | inconsistent across doses | low cells (technical?) |
| [[EX229 (drug)]] 5 µM |  | 0.630× | -3.2 | 0.26 | 8/38 (LS 180, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | 0.642× | -3.1 | 0.30 | 5/42 (HEC-1-A, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15477. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 4.57 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.44× (z +9.1) | [[Erlotinib (drug)]] 5 µM 0.0540× (z -10.8) |
| [[LoVo (line)]] | wt | 5.93 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.33× (z +9.7) | — |
| [[A-172 (line)]] | wt | 3.94 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.04× (z +11.2) | — |
| [[A498 (line)]] | wt | 2.37 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.38× (z +9.4) | — |
| [[HEC-1-A (line)]] | alt | 8.61 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.99× (z +9.0) | — |
| [[HOP62 (line)]] | alt | 10.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.79× (z +11.1) | — |
| [[J82 (line)]] | alt | 4.75 | 0 | 1 | — | [[LJI308 (drug)]] 0.05 µM 0.0599× (z -10.5) |
| [[LOX-IMVI (line)]] | wt | 3.93 | 0 | 1 | — | [[Elagolix sodium (drug)]] 0.5 µM 0.0671× (z -10.0) |
| [[PANC-1 (line)]] | alt | 4.99 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.47× (z +10.5) | — |
| [[SW480 (line)]] | alt | 6.66 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.26× (z +9.3) | — |
| [[A-427 (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.81 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.99 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.69 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.97 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.59 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.89 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.10 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.02 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.65 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.31 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.53 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.05 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.95 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.44 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.12 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.89 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.46 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.75 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.18 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.75 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.62 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.31 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.71 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.34 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.92 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.40 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.27 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.71 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.55 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.05 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.81 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.89 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.86 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.13 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15477), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HSPA2-AS1]] | +0.76 | +0.69 / +0.65 | both halves | 7e-06 | same gene group |
| [[CHMP3-AS1]] | +0.76 | +0.65 / +0.71 | both halves | 7e-06 | same gene group |
| [[UPK2]] | +0.76 | +0.69 / +0.72 | both halves | 7e-06 |  |
| [[SYNM-AS1]] | +0.75 | +0.76 / +0.63 | both halves | 7e-06 | same gene group |
| [[PAXBP1-AS1]] | +0.75 | +0.76 / +0.65 | both halves | 7e-06 | same gene group |
| [[CTDSPL2-DT]] | +0.74 | +0.70 / +0.69 | both halves | 7e-06 |  |
| [[PPP1R9A-AS1]] | +0.73 | +0.76 / +0.59 | both halves | 7e-06 | same gene group |
| [[STX17-DT]] | +0.73 | +0.72 / +0.63 | both halves | 7e-06 |  |
| [[CNGB3]] | +0.72 | +0.66 / +0.62 | both halves | 7e-06 |  |
| [[OSER1-DT]] | +0.72 | +0.71 / +0.70 | both halves | 7e-06 |  |
| [[RBMS3-AS3]] | +0.72 | +0.78 / +0.53 | both halves | 1e-05 | same gene group |
| [[TTC36-AS1]] | +0.71 | +0.73 / +0.63 | both halves | 7e-06 | same gene group |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TCOF1]] | -0.69 | -0.59 / -0.61 | both halves | 7e-06 |  |
| [[FBXW2]] | -0.63 | -0.72 / -0.44 | both halves | 3e-05 |  |
| [[HERC2]] | -0.63 | -0.51 / -0.56 | both halves | 1e-05 |  |
| [[HERC2P9]] | -0.61 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[RRP1B]] | -0.61 | -0.53 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers NDUFV2-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PKD1L2]] | B | PKD1L2 activity raises NDUFV2-AS1's level | lines that do not express PKD1L2 (13) vs lines expressing it (37) | 1.23× lower at baseline in the lines without PKD1L2 | 0.056 | ⚠ within organs, on part of the lines; also absent: SPDYE10; maybe low, not absent |
| [[TTN]] | C | TTN activity lowers NDUFV2-AS1's level | lines that do not express TTN (4) vs lines expressing it (46) | 1.51× higher at baseline in the lines without TTN | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ZSWIM5; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.720). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (9.8, 23.9); signed map (32.2, -1.5). **Vector** length 52.4, 6.61% of its response variance represented; |z| ≥ 3 in 940 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.4 | +21.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.5 | +18.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.6 | +4.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.3 | +4.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.3 | +4.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.4 | +4.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.7 | +7.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.3 | +4.6 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.3 | +2.4 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +1.3 | +2.0 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.5 | -4.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | -0.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.6 | -3.1 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.5 | -2.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -1.3 | -2.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.3 | -0.5 |
|  | [[venetoclax (drug)]] 5 µM |  | -1.2 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | NDUFV2 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 18p11.22 — chr18:9,121,179-9,136,645 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:50826](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:50826) · Entrez [101927275](https://www.ncbi.nlm.nih.gov/gene/101927275) · Ensembl [ENSG00000266053](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000266053)

## Data

Gene col 15477: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15477); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15477, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15477]; `tensor/DDL_lfc|DDL_z.npy` [15477]; `embed/gene_vectors.npy` [15477]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15477 or target_col == 15477). Every well: [[NDUFV2-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NDUFV2-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
