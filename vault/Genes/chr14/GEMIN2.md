---
symbol: "GEMIN2"
type: "gene"
col: 1696
ensembl_id: "ENSG00000092208"
name: "gem nuclear organelle associated protein 2"
location: "14q21.1"
module: 17
arm: "+"
pooled_cpm: 9.03
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 5
n_dd_up_clean: 15
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# GEMIN2

*gem nuclear organelle associated protein 2* — 14q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.85× (z +9.4, q 3e-18, up in 37 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.625× (z -7.2, q 3e-10, down in 23 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EBAG9]] (+0.75, fdr 7e-06), [[MRPS31P4]] (+0.73, fdr 7e-06), [[RP9]] (+0.73, fdr 7e-06); moves opposite to [[SLC25A53]] (-0.65, fdr 1e-05), [[HCFC1]] (-0.63, fdr 1e-05), [[CASTOR3P-1]] (-0.58, fdr 5e-05).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PLEKHA6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 3 with an alert ⚠. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1696.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.85×** | +9.4 | 3e-18 | 37/47 (LoVo, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.88×** | +9.3 | 3e-18 | 28/46 (SW480, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.72×** | +8.3 | 2e-14 | 31/47 (LoVo, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.69×** | +8.0 | 2e-13 | 28/47 (BT-474, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.66×** | +7.8 | 1e-12 | 30/46 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.60×** | +7.2 | 6e-11 | 25/44 (NCI-H1792, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.54×** | +6.4 | 1e-08 | 19/38 (NCI-H2030, SW1417, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.44×** | +5.6 | 1e-06 | 19/47 (HEC-1-A, KATO III, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.40×** | +5.1 | 2e-05 | 12/47 (LS 180, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.24×** | +4.6 | 2e-04 | 15/48 (NCI-H1573, LOX-IMVI, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.38×** | +4.6 | 3e-04 | 16/43 (HEC-1-A, AsPC-1, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.32×** | +4.3 | 9e-04 | 11/43 (HT-29, LoVo, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **1.22×** | +4.2 | 9e-04 | 20/46 (A-427, NCI-H2030, …) | all doses, flat | composition shift |
| [[Verteporfin (drug)]] 5 µM |  | **1.29×** | +3.7 | 0.008 | 11/45 (NCI-H23, NCI-H1792, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~37% of this change | **1.26×** | +3.5 | 0.015 | 9/39 (Panc 03.27, HCT15, …) | inconsistent across doses | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | **1.23×** | +3.2 | 0.047 | 1/47 (SNU-423) | top dose only |  |
| [[Ixazomib (drug)]] 0.05 µM |  | **1.24×** | +3.1 | 0.073 | 5/44 (HS-578T, A-427, …) | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.32×** | +3.0 | 0.083 | 5/38 (PANC-1, LS 180, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1696.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.625×** | -7.2 | 3e-10 | 23/47 (SW480, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.676×** | -6.0 | 6e-07 | 22/47 (HOP62, HEC-1-A, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.708×** | -5.3 | 2e-05 | 20/46 (BT-474, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.746×** | -4.5 | 0.001 | 21/47 (SHP-77, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.752×** | -4.2 | 0.003 | 12/16 (J82, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Cyclosporin A (drug)]] 0.5 µM |  | 0.810× | -3.2 | 0.12 | 11/46 (C32, BT-474, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~7% of this change | 0.814× | -3.2 | 0.12 | 11/47 (HS-578T, J82, …) | top dose only |  |
| [[9-ING-41 (drug)]] 0.05 µM |  | 0.805× | -3.1 | 0.12 | 1/48 (NCI-H460) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1696. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 7.90 | 0 | 2 (1 ⚠) | — | [[(R)-Verapamil (hydrochloride) (drug)]] 0.5 µM 0.0929× (z -10.5) |
| [[A-172 (line)]] | wt | 5.33 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.116× (z -8.7) |
| [[AsPC-1 (line)]] | alt | 3.93 | 0 | 1 | — | [[Rosiglitazone (drug)]] 5 µM 0.0832× (z -8.7) |
| [[HEC-1-A (line)]] | alt | 10.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.197× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 9.10 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0864× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HS-578T (line)]] | alt | 7.14 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.261× (z -8.7) ⚠ cell-cycle shift, explains ~92% of this change |
| [[J82 (line)]] | alt | 8.61 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.171× (z -9.0) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 6.56 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0834× (z -10.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-1 (line)]] | wt | 8.90 | 0 | 1 | — | [[Cabozantinib (S-malate) (drug)]] 0.5 µM 0.0553× (z -10.0) |
| [[A-427 (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 8.15 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.59 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.90 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.80 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.10 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.65 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.98 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.45 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.37 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.71 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.97 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.03 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.27 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.90 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 7.21 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.41 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.29 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 9.45 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 9.40 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.40 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.76 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.32 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.85 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 10.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1696), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EBAG9]] | +0.75 | +0.70 / +0.75 | both halves | 7e-06 |  |
| [[MRPS31P4]] | +0.73 | +0.74 / +0.65 | both halves | 7e-06 |  |
| [[RP9]] | +0.73 | +0.73 / +0.66 | both halves | 7e-06 |  |
| [[RIOK2]] | +0.72 | +0.70 / +0.69 | both halves | 7e-06 |  |
| [[EXOSC9]] | +0.71 | +0.64 / +0.71 | both halves | 7e-06 |  |
| [[SAAL1]] | +0.71 | +0.71 / +0.63 | both halves | 7e-06 |  |
| [[METTL14]] | +0.70 | +0.67 / +0.69 | both halves | 7e-06 |  |
| [[TRAPPC11]] | +0.69 | +0.70 / +0.62 | both halves | 7e-06 |  |
| [[MRPS31]] | +0.69 | +0.70 / +0.70 | both halves | 7e-06 |  |
| [[TARS2]] | +0.68 | +0.67 / +0.60 | both halves | 7e-06 |  |
| [[KBTBD6]] | +0.68 | +0.56 / +0.69 | both halves | 1e-05 |  |
| [[PRPF39]] | +0.68 | +0.65 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC25A53]] | -0.65 | -0.54 / -0.65 | both halves | 1e-05 |  |
| [[HCFC1]] | -0.63 | -0.57 / -0.57 | both halves | 1e-05 |  |
| [[CASTOR3P-1]] | -0.58 | -0.40 / -0.54 | both halves | 5e-05 |  |
| [[DNAJB6]] | -0.58 | -0.37 / -0.67 | both halves | 8e-05 |  |
| [[SLIT2]] | -0.58 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[SFXN5]] | -0.58 | -0.47 / -0.61 | both halves | 2e-05 |  |
| [[ZNF407]] | -0.56 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[RAB22A]] | -0.56 | -0.47 / -0.59 | both halves | 2e-05 |  |
| [[CCNT2-AS1]] | -0.56 | -0.32 / -0.50 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLEKHA6]] | B | PLEKHA6 activity lowers GEMIN2's level | lines that do not express PLEKHA6 (16) vs lines expressing it (34) | 1.17× higher at baseline in the lines without PLEKHA6 | 0.090 | ⚠ within organs, on part of the lines; also absent: KCNK1, ELF3, TNK1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.776). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-26.9, -1.6); signed map (-21.4, -14.7). **Vector** length 72.3, 11.8% of its response variance represented; |z| ≥ 3 in 934 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +4.8 | +7.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.9 | +9.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.3 | +5.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +2.6 | +7.2 |
|  | [[Selinexor (drug)]] 5 µM |  | +2.5 | +4.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.3 | +4.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.9 | +3.7 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +1.5 | +2.1 |
|  | [[Bexarotene (drug)]] 5 µM |  | +1.4 | +2.3 |
| fall | [[Auranofin (drug)]] 5 µM |  | -5.5 | -6.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~92% of this change | -4.2 | +0.7 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.7 | -7.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.7 | -4.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.2 | -5.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.1 | -1.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.7 | -1.4 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.6 | -2.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.5 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | gem nuclear organelle associated protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q21.1 — chr14:39,114,285-39,136,973 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously SIP1 |
| Gene groups (HGNC) | Gemins |
| Reactome | 8 pathways, smallest: SARS-CoV-2 modulates host translation machinery; Metabolism of non-coding RNA; snRNP Assembly |
| Matched by | ensembl_id |

**Function**, from UniProt [O14893](https://www.uniprot.org/uniprotkb/O14893) (Gem-associated protein 2):

> The SMN complex catalyzes the assembly of small nuclear ribonucleoproteins (snRNPs), the building blocks of the spliceosome, and thereby plays an important role in the splicing of cellular pre-mRNAs. Most spliceosomal snRNPs contain a common set of Sm proteins SNRPB, SNRPD1, SNRPD2, SNRPD3, SNRPE, SNRPF and SNRPG that assemble in a heptameric protein ring on the Sm site of the small nuclear RNA to form the core snRNP (Sm core). In the cytosol, the Sm proteins SNRPD1, SNRPD2, SNRPE, SNRPF and …

**Summary**, from NCBI Gene [8487](https://www.ncbi.nlm.nih.gov/gene/8487):

> This gene encodes one of the proteins found in the SMN complex, which consists of several gemin proteins and the protein known as the survival of motor neuron protein. The SMN complex is localized to a subnuclear compartment called gems (gemini of coiled bodies) and is required for assembly of spliceosomal snRNPs and for pre-mRNA splicing. This protein interacts directly with the survival of motor neuron protein and it is required for formation of the SMN complex. A knockout mouse targeting the …

**Accessions** — [HGNC:10884](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10884) · Entrez [8487](https://www.ncbi.nlm.nih.gov/gene/8487) · UniProt [O14893](https://www.uniprot.org/uniprotkb/O14893) · Ensembl [ENSG00000092208](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000092208)

## Data

Gene col 1696: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1696); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1696, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1696]; `tensor/DDL_lfc|DDL_z.npy` [1696]; `embed/gene_vectors.npy` [1696]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1696 or target_col == 1696). Every well: [[GEMIN2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GEMIN2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
