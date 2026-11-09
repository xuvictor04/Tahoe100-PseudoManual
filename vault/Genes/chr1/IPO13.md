---
symbol: "IPO13"
type: "gene"
col: 3903
ensembl_id: "ENSG00000117408"
name: "importin 13"
location: "1p34.1"
module: 2
arm: "+"
pooled_cpm: 6.1
n_lines_expressing: 50
n_dd_up: 31
n_dd_down: 4
n_dd_up_clean: 17
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# IPO13

*importin 13* — 1p34.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (14 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 3.17× (z +14.5, q 7e-45, up in 40 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 0.706× (z -4.4, q 0.006, down in 15 of 45 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[B4GALT7]] (+0.68, fdr 2e-05), [[LZTR1]] (+0.61, fdr 1e-05), [[LRRC14]] (+0.61, fdr 1e-05); moves opposite to [[DEPTOR]] (-0.52, fdr 9e-05), [[FAM81A]] (-0.49, fdr 6e-05), [[PNISR]] (-0.49, fdr 3e-04).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 15 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3903.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **3.17×** | +14.5 | 7e-45 | 40/47 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.23×** | +14.2 | 2e-43 | 30/39 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **3.03×** | +13.9 | 6e-42 | 40/47 (PANC-1, SW480, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **2.45×** | +11.3 | 3e-27 | 36/47 (SW480, PANC-1, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.83×** | +10.8 | 6e-25 | 26/41 (RKO, SW480, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.82×** | +7.5 | 5e-12 | 25/47 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **1.84×** | +7.4 | 2e-11 | 21/43 (SW480, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.81×** | +7.2 | 5e-11 | 18/38 (NCI-H460, A549, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **1.81×** | +7.1 | 6e-11 | 5/9 (A498, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.69×** | +6.6 | 3e-09 | 18/38 (A-172, H4, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.65×** | +6.3 | 2e-08 | 20/45 (A549, SNU-423, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.65×** | +6.3 | 2e-08 | 19/39 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~43% of this change | **1.67×** | +6.2 | 2e-08 | 10/31 (HT-29, PANC-1, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.63×** | +5.9 | 1e-07 | 19/38 (LS 180, LoVo, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.60×** | +5.6 | 1e-06 | 15/43 (PANC-1, H4, …) | inconsistent across doses | cell-cycle shift (explains ~14% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.29×** | +4.5 | 2e-04 | 9/46 (PANC-1, NCI-H460, …) | rises with dose | position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **1.86×** | +4.1 | 0.001 | 7/44 (PANC-1, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Pyridoxine (drug)]] 0.5 µM |  | **1.33×** | +3.6 | 0.008 | 6/39 (A-172, LS 180, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.31×** | +3.4 | 0.016 | 11/43 (PANC-1, LS 180, …) | rises with dose |  |
| [[Erlotinib (drug)]] 5 µM |  | **1.29×** | +3.0 | 0.045 | 3/44 (NCI-H2030, hTERT-HPNE, …) | top dose only |  |
| [[Canagliflozin (drug)]] 0.05 µM |  | **1.32×** | +3.0 | 0.048 | 3/38 (SW 900, NCI-H2030, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3903.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.706×** | -4.4 | 0.006 | 15/45 (NCI-H1792, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.718×** | -4.2 | 0.007 | 15/45 (AN3 CA, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.736×** | -3.9 | 0.019 | 17/40 (A-172, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.05 µM |  | **0.766×** | -3.4 | 0.099 | 6/45 (hTERT-HPNE, NCI-H1573, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | 0.783× | -3.1 | 0.21 | 11/43 (Panc 03.27, HCT15, …) | inconsistent across doses |  |
| [[Almonertinib (mesylate) (drug)]] 5 µM |  | 0.781× | -3.0 | 0.24 | 2/46 (AN3 CA, LOX-IMVI) | top dose only | plate-row cell shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.54 per unit of S-phase module lfc, -0.40 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3903. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 6.93 | 1 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.53× (z +8.5) ⚠ cell-cycle shift, explains ~26% of this change | [[Lonafarnib (drug)]] 5 µM 0.0489× (z -10.7) ⚠ toxic |
| [[A-172 (line)]] | wt | 10.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.152× (z -10.1) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 8.42 | 0 | 1 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.0835× (z -9.2) ⚠ cell-cycle shift, explains ~62% of this change |
| [[SW480 (line)]] | alt | 5.74 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.23× (z +9.5) | — |
| [[A-427 (line)]] | wt | 6.13 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.48 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.14 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.78 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.24 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.48 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.01 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.96 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.46 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.96 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.66 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.99 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.12 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.38 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.33 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.33 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.75 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.30 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.64 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.39 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.42 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.68 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.31 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.19 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.35 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.26 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.08 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.59 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.27 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.40 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.70 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.05 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.20 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.57 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.41 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.48 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.55 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.09 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3903), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[B4GALT7]] | +0.68 | +0.47 / +0.64 | both halves | 2e-05 |  |
| [[LZTR1]] | +0.61 | +0.53 / +0.63 | both halves | 1e-05 |  |
| [[LRRC14]] | +0.61 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[MAPK7]] | +0.60 | +0.39 / +0.52 | both halves | 6e-05 |  |
| [[FAM3A]] | +0.59 | +0.44 / +0.59 | both halves | 3e-05 |  |
| [[TINF2]] | +0.58 | +0.46 / +0.54 | both halves | 3e-05 |  |
| [[SGTA]] | +0.58 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[ELOVL1]] | +0.58 | +0.38 / +0.58 | both halves | 6e-05 |  |
| [[RHBDF1]] | +0.58 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[CEP170B]] | +0.58 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[CIC]] | +0.57 | +0.59 / +0.48 | both halves | 2e-05 |  |
| [[SLC12A4]] | +0.57 | +0.44 / +0.59 | both halves | 3e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DEPTOR]] | -0.52 | -0.37 / -0.41 | both halves | 9e-05 |  |
| [[FAM81A]] | -0.49 | -0.44 / -0.39 | both halves | 6e-05 |  |
| [[PNISR]] | -0.49 | -0.28 / -0.52 | both halves | 3e-04 |  |
| [[LINC00173]] | -0.48 | -0.30 / -0.44 | both halves | 2e-04 |  |
| [[PTMA]] | -0.46 | -0.48 / -0.40 | both halves | 5e-05 |  |
| [[RHOXF1]] | -0.46 | -0.49 / -0.39 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers IPO13's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.9% of all compounds | 0.044 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.448). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-10.3, -26.3); signed map (-25.0, 2.7). **Vector** length 58.9, 8.52% of its response variance represented; |z| ≥ 3 in 989 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +3.0 | +14.2 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +2.9 | +4.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.7 | +5.0 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | +2.2 | +1.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +2.1 | +6.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.0 | +1.9 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.9 | +1.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.8 | +3.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | +1.7 | +0.6 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.6 | +1.7 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.0 | +0.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -2.7 | -3.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.0 | -3.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.9 | -1.8 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.7 | -0.7 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.6 | -3.4 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -1.3 | -2.0 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.2 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | importin 13 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p34.1 — chr1:43,946,950-43,968,022 (+) |
| Ensembl biotype | protein_coding |
| Also known as | IMP13, KIAA0724, RANBP13 |
| Gene groups (HGNC) | Importins |
| Matched by | ensembl_id |

**Function**, from UniProt [O94829](https://www.uniprot.org/uniprotkb/O94829) (Importin-13):

> Functions in nuclear protein import as nuclear transport receptor. Serves as receptor for nuclear localization signals (NLS) in cargo substrates. Is thought to mediate docking of the importin/substrate complex to the nuclear pore complex (NPC) through binding to nucleoporin and the complex is subsequently translocated through the pore by an energy requiring, Ran-dependent mechanism. At the nucleoplasmic side of the NPC, Ran binds to the importin, the importin/substrate complex dissociates and …

**Summary**, from NCBI Gene [9670](https://www.ncbi.nlm.nih.gov/gene/9670):

> This gene encodes a member of the importin-beta family of nuclear transport proteins. The encoded protein mediates the import of specific cargo proteins from the cytoplasm to the nucleus and is dependent on the Ras-related nuclear protein-GTPase system. The encoded protein is also involved in nuclear export of the eukaryotic translation initiation factor 1A.[provided by RefSeq, Mar 2009]

**Accessions** — [HGNC:16853](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16853) · Entrez [9670](https://www.ncbi.nlm.nih.gov/gene/9670) · UniProt [O94829](https://www.uniprot.org/uniprotkb/O94829) · Ensembl [ENSG00000117408](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000117408)

## Data

Gene col 3903: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3903); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3903, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3903]; `tensor/DDL_lfc|DDL_z.npy` [3903]; `embed/gene_vectors.npy` [3903]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3903 or target_col == 3903). Every well: [[IPO13 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IPO13.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
