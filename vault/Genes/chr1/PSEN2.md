---
symbol: "PSEN2"
type: "gene"
col: 6807
ensembl_id: "ENSG00000143801"
name: "presenilin 2"
location: "1q42.13"
module: 1
arm: "+"
pooled_cpm: 9.48
n_lines_expressing: 49
n_dd_up: 31
n_dd_down: 0
n_dd_up_clean: 23
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# PSEN2

*presenilin 2* — 1q42.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.91× (z +13.4, q 4e-38, up in 39 of 46 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 2 lines (SNU-1 0.109×, SW48 0.148×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change); [[Cyclosporin A (drug)]] 0.5 µM in 1 line (KATO III 0.0489×); [[Simotinib (drug)]] 5 µM in 1 line (SW48 0.0851×; ⚠ toxic); [[Resveratrol (drug)]] 0.5 µM in 1 line (SNU-1 0.0638×); [[Silodosin (drug)]] 5 µM in 1 line (A498 0.140×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PTPN21]] (+0.64, fdr 7e-06), [[RIOX2]] (+0.62, fdr 1e-05), [[RPS6KA4]] (+0.61, fdr 2e-05); moves opposite to [[PMS2P4-1]] (-0.55, fdr 1e-05), [[SNHG31]] (-0.55, fdr 1e-04), [[MED6]] (-0.54, fdr 1e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[ABCA3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6807.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.91×** | +13.4 | 4e-38 | 39/46 (CFPAC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.62×** | +12.1 | 5e-31 | 39/46 (CFPAC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **2.24×** | +10.1 | 8e-22 | 37/46 (LoVo, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.68×** | +9.2 | 5e-18 | 33/46 (SW480, HEC-1-A, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.83×** | +7.6 | 4e-12 | 33/46 (SW480, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.82×** | +7.5 | 7e-12 | 21/35 (LoVo, NCI-H1573, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.77×** | +6.9 | 4e-10 | 28/44 (A-172, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.63×** | +5.9 | 3e-07 | 8/17 (NCI-H2347, PANC-1, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.37×** | +5.6 | 1e-06 | 17/43 (SW 900, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.59×** | +5.5 | 2e-06 | 18/39 (A-172, LS 180, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.53×** | +5.3 | 5e-06 | 23/46 (NCI-H460, C32, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.52×** | +5.2 | 8e-06 | 20/46 (A-172, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.49×** | +5.0 | 2e-05 | 19/46 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.05×** | +4.7 | 1e-04 | 17/46 (SW480, SW 900, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.41×** | +4.3 | 6e-04 | 17/43 (SW480, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 5 µM |  | **1.42×** | +4.2 | 0.001 | 15/44 (NCI-H1573, NCI-H460, …) | rises with dose | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.40×** | +4.1 | 0.001 | 18/43 (CFPAC-1, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **1.40×** | +4.0 | 0.002 | 15/45 (C32, A-172, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.37×** | +4.0 | 0.002 | 11/46 (COLO 205, SW480, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6807.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 2 lines (SNU-1 0.109×, SW48 0.148×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change); [[Cyclosporin A (drug)]] 0.5 µM in 1 line (KATO III 0.0489×); [[Simotinib (drug)]] 5 µM in 1 line (SW48 0.0851×; ⚠ toxic); [[Resveratrol (drug)]] 0.5 µM in 1 line (SNU-1 0.0638×); [[Silodosin (drug)]] 5 µM in 1 line (A498 0.140×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | 0.622× | -3.1 | 0.96 | 9/44 (SNU-1, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~19% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, -0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6807. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-1 (line)]] | wt | 13.5 | 0 | 3 (1 ⚠) | — | [[Resveratrol (drug)]] 0.5 µM 0.0638× (z -10.6) |
| [[A498 (line)]] | wt | 8.92 | 1 (1 ⚠) | 1 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 5.90× (z +9.5) ⚠ cell-cycle shift, explains ~0% of this change | [[Silodosin (drug)]] 5 µM 0.140× (z -10.5) |
| [[SW48 (line)]] | wt | 19.5 | 0 | 2 (2 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.0851× (z -10.8) ⚠ toxic |
| [[KATO III (line)]] | alt | 4.65 | 0 | 1 | — | [[Cyclosporin A (drug)]] 0.5 µM 0.0489× (z -11.0) |
| [[NCI-H1573 (line)]] | alt | 7.01 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.0883× (z -10.0) |
| [[NCI-H2030 (line)]] | alt | 14.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.156× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 10.2 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.124× (z -8.5) |
| [[A-172 (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.88 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.45 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.68 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.60 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.47 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.57 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.28 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.29 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.51 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.60 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.83 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.08 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.73 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 9.59 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.64 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.97 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.01 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.77 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.83 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.28 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 8.86 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.36 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 8.51 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 21.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.87 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.86 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.88 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.44 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 12.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6807), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTPN21]] | +0.64 | +0.59 / +0.68 | both halves | 7e-06 |  |
| [[RIOX2]] | +0.62 | +0.56 / +0.68 | both halves | 1e-05 |  |
| [[RPS6KA4]] | +0.61 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[PINX1]] | +0.58 | +0.53 / +0.63 | both halves | 1e-05 |  |
| [[MAPKAPK3]] | +0.58 | +0.37 / +0.60 | both halves | 9e-05 |  |
| [[TXNRD3]] | +0.57 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[NBPF20]] | +0.56 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[SLC36A1]] | +0.56 | +0.52 / +0.68 | both halves | 1e-05 |  |
| [[ABCA3]] | +0.56 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[BMP2K]] | +0.56 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[ZNF783]] ⚠ | +0.55 | +0.54 / +0.57 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[PDCD2]] | +0.55 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[USP31]] | +0.55 | +0.50 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PMS2P4-1]] | -0.55 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[SNHG31]] | -0.55 | -0.35 / -0.65 | both halves | 1e-04 |  |
| [[MED6]] | -0.54 | -0.52 / -0.55 | both halves | 1e-05 |  |
| [[CDKN2C]] | -0.54 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[TTC28-AS1]] | -0.53 | -0.50 / -0.43 | both halves | 3e-05 |  |
| [[HELZ]] | -0.52 | -0.57 / -0.50 | both halves | 1e-05 |  |
| [[TENT5A]] | -0.52 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[KLHL3]] | -0.52 | -0.36 / -0.58 | both halves | 1e-04 |  |
| [[NSD3]] | -0.52 | -0.41 / -0.56 | both halves | 4e-05 |  |
| [[TMUB2]] | -0.50 | -0.48 / -0.55 | both halves | 2e-05 |  |
| [[ADAM20]] | -0.50 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[EMSY]] | -0.50 | -0.39 / -0.57 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ABCA3]] | B | ABCA3 activity raises PSEN2's level | lines that do not express ABCA3 (9) vs lines expressing it (41) | 1.68× lower at baseline in the lines without ABCA3 | 0.055 | ⚠ within organs, on part of the lines; also absent: SLC37A1, CCDC88C, GRTP1; maybe low, not absent |
| [[CA9]] | B | CA9 activity lowers PSEN2's level | lines that do not express CA9 (19) vs lines expressing it (31) | 1.44× higher at baseline in the lines without CA9 | 0.087 | ⚠ within organs, on part of the lines; also absent: ENSG00000289153, IL2RG, LINC02970 |
| [[TENT5A]] | B | TENT5A activity lowers PSEN2's level | lines that do not express TENT5A (11) vs lines expressing it (39) | 1.76× higher at baseline in the lines without TENT5A | 0.091 | ⚠ within organs, on part of the lines; also absent: GBP2, CXCL2, IFI44; maybe low, not absent |
| [[EPHA10]] | B | EPHA10 activity raises PSEN2's level | lines that do not express EPHA10 (19) vs lines expressing it (31) | 1.55× lower at baseline in the lines without EPHA10 | 0.099 | ⚠ within organs, on part of the lines; also absent: LSR, OCLN, ENTPD2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.483). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-9.4, -27.6); signed map (-0.9, -40.6). **Vector** length 79.4, 14.8% of its response variance represented; |z| ≥ 3 in 1,081 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.6 | +5.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.7 | +7.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.5 | +9.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.3 | +3.1 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +4.2 | +3.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.7 | +3.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.7 | +4.2 |
| fall | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.1 | -2.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.9 | -0.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.8 | +2.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.5 | -1.8 |
|  | [[TAK-901 (drug)]] 5 µM |  | -2.1 | -3.1 |
|  | [[Relugolix (drug)]] 0.5 µM |  | -1.6 | -2.6 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.6 | -1.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.3 | -0.5 |
|  | [[Arbutin (drug)]] 5 µM |  | -1.2 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | presenilin 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q42.13 — chr1:226,870,184-226,927,726 (+) |
| Ensembl biotype | protein_coding |
| Also known as | AD3L, STM2, PS2, PS-2, E5-1; previously AD4 |
| Gene groups (HGNC) | Presenilin family; Gamma-secretase complex subunits |
| Hallmark sets | NOTCH_SIGNALING, WNT_BETA_CATENIN_SIGNALING, MYOGENESIS, APOPTOSIS |
| Reactome | 32 pathways, smallest: Noncanonical activation of NOTCH3; NOTCH4 Activation and Transmission of Signal to the Nucleus; Regulated proteolysis of p75NTR |
| Matched by | ensembl_id |

**Function**, from UniProt [P49810](https://www.uniprot.org/uniprotkb/P49810) (Presenilin-2):

> Catalytic subunit of the gamma-secretase complex, an endoprotease complex that catalyzes the intramembrane cleavage of integral membrane proteins such as Notch receptors and APP (amyloid-beta precursor protein). Selectively cleaves late endosomal/lysosomal localized substrates and generates the prominent pool of intracellular amyloid beta that contains longer amyloid beta. The holoprotein functions as a calcium-leak channel that allows the passive movement of calcium from endoplasmic reticulum …

**Summary**, from NCBI Gene [5664](https://www.ncbi.nlm.nih.gov/gene/5664):

> Alzheimer's disease (AD) patients with an inherited form of the disease carry mutations in the presenilin proteins (PSEN1 or PSEN2) or the amyloid precursor protein (APP). These disease-linked mutations result in increased production of the longer form of amyloid-beta (main component of amyloid deposits found in AD brains). Presenilins are postulated to regulate APP processing through their effects on gamma-secretase, an enzyme that cleaves APP. Also, it is thought that the presenilins are …

**Accessions** — [HGNC:9509](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9509) · Entrez [5664](https://www.ncbi.nlm.nih.gov/gene/5664) · UniProt [P49810](https://www.uniprot.org/uniprotkb/P49810) · Ensembl [ENSG00000143801](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143801)

## Data

Gene col 6807: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6807); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6807, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6807]; `tensor/DDL_lfc|DDL_z.npy` [6807]; `embed/gene_vectors.npy` [6807]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6807 or target_col == 6807). Every well: [[PSEN2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PSEN2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
