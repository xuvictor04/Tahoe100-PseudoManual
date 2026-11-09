---
symbol: "ZBTB24"
type: "gene"
col: 3363
ensembl_id: "ENSG00000112365"
name: "zinc finger and BTB domain containing 24"
location: "6q21"
module: 1
arm: "+"
pooled_cpm: 14.64
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 7
n_dd_up_clean: 5
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# ZBTB24

*zinc finger and BTB domain containing 24* — 6q21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 1.83× (z +9.8, q 6e-20, up in 29 of 42 measured lines) ⚠ toxic. The strongest without an alert is [[Ponatinib (drug)]] 5 µM: 1.40× (z +5.6, q 3e-06, up in 19 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.637× (z -7.6, q 1e-11, down in 23 of 38 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.621× (z -4.2, q 0.003, down in 12 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KAT14]] (+0.72, fdr 1e-05), [[POGK]] (+0.70, fdr 7e-06), [[MRPL15]] (+0.68, fdr 7e-06); moves opposite to [[MAGT1]] (-0.54, fdr 1e-05), [[APLP2]] (-0.54, fdr 1e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[LTBR]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3363.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.83×** | +9.8 | 6e-20 | 29/42 (HT-29, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.40×** | +5.6 | 3e-06 | 19/48 (PANC-1, SNU-423, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.40×** | +5.6 | 3e-06 | 19/47 (SNU-423, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.36×** | +5.2 | 3e-05 | 16/47 (J82, PANC-1, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.34×** | +4.8 | 2e-04 | 11/47 (A-427, SHP-77, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.32×** | +4.7 | 3e-04 | 15/47 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.20×** | +4.3 | 0.001 | 13/48 (NCI-H2347, HT-29, …) | rises with dose | low cells (technical?) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.31×** | +4.3 | 0.001 | 13/47 (PANC-1, A498, …) | inconsistent across doses |  |
| [[venetoclax (drug)]] 5 µM |  | 1.41× | +3.0 | 0.15 | 6/43 (SK-MEL-2, SHP-77, …) | inconsistent across doses | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | 1.41× | +3.0 | 0.15 | 6/44 (MIA PaCa-2, NCI-H2030, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3363.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.637×** | -7.6 | 1e-11 | 23/38 (PANC-1, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.633×** | -7.4 | 3e-11 | 17/25 (HEC-1-A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.655×** | -7.2 | 1e-10 | 25/46 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.680×** | -6.5 | 1e-08 | 24/47 (SW 900, SW480, …) | rises with dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.621×** | -4.2 | 0.003 | 12/48 (PANC-1, NCI-H2030, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.773×** | -4.2 | 0.003 | 18/47 (LS 180, SNU-423, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Ritonavir (drug)]] 0.5 µM |  | **0.825×** | -3.3 | 0.091 | 14/47 (J82, CHP-212, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3363. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 16.5 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.152× (z -10.2) ⚠ toxic; cell-cycle shift, explains ~40% of this change · without an alert: [[Oxaprozin (drug)]] 0.5 µM 0.164× (z -10.1) |
| [[PANC-1 (line)]] | alt | 36.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.180× (z -20.3) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 16.5 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.192× (z -10.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 7.40 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.191× (z -10.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 16.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.173× (z -12.8) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 10.3 | 0 | 1 | — | [[Raltitrexed (drug)]] 0.5 µM 0.0513× (z -14.3) |
| [[HT-29 (line)]] | alt | 11.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.150× (z -10.7) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 16.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.248× (z -9.0) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 16.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.235× (z -9.3) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 15.9 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.246× (z -8.6) ⚠ cell-cycle shift, explains ~8% of this change |
| [[NCI-H1573 (line)]] | alt | 6.99 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0784× (z -12.4) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 10.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0610× (z -19.4) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 9.66 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.194× (z -8.6) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 12.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.120× (z -9.5) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 14.8 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.5 µM 0.0924× (z -12.7) |
| [[SW 900 (line)]] | alt | 8.84 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.117× (z -9.5) ⚠ cell-cycle shift, explains ~25% of this change |
| [[SW48 (line)]] | wt | 13.9 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.112× (z -9.2) |
| [[SW480 (line)]] | alt | 18.6 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.352× (z -9.4) ⚠ cell-cycle shift, explains ~25% of this change |
| [[A-172 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.98 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.98 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.79 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.48 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 20.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.99 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.69 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 19.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.64 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3363), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KAT14]] | +0.72 | +0.57 / +0.75 | both halves | 1e-05 |  |
| [[POGK]] | +0.70 | +0.65 / +0.68 | both halves | 7e-06 |  |
| [[MRPL15]] | +0.68 | +0.70 / +0.61 | both halves | 7e-06 |  |
| [[LTV1]] | +0.68 | +0.65 / +0.65 | both halves | 7e-06 |  |
| [[SCO1]] | +0.67 | +0.61 / +0.68 | both halves | 7e-06 |  |
| [[ZNF202]] | +0.66 | +0.60 / +0.62 | both halves | 7e-06 | same gene group |
| [[BYSL]] | +0.65 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[NUDT19]] | +0.65 | +0.56 / +0.68 | both halves | 1e-05 |  |
| [[UMPS]] | +0.64 | +0.58 / +0.66 | both halves | 7e-06 |  |
| [[RIOX2]] | +0.64 | +0.73 / +0.54 | both halves | 1e-05 |  |
| [[RDH14]] | +0.64 | +0.68 / +0.56 | both halves | 1e-05 |  |
| [[ZBTB39]] | +0.63 | +0.54 / +0.64 | both halves | 1e-05 | same gene group |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAGT1]] | -0.54 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[APLP2]] | -0.54 | -0.52 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LTBR]] | B | LTBR activity lowers ZBTB24's level | lines that do not express LTBR (8) vs lines expressing it (42) | 1.27× higher at baseline in the lines without LTBR | 0.071 | ⚠ within organs, on part of the lines; also absent: SIGIRR, YPEL3, CLCF1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.620). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-47.6, -7.2); signed map (-1.3, -41.0). **Vector** length 74.6, 12.3% of its response variance represented; |z| ≥ 3 in 888 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +6.0 | +9.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.8 | +4.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +4.4 | +5.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.6 | +2.8 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.1 | +2.0 |
|  | [[EX229 (drug)]] 5 µM |  | +2.4 | +2.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.4 | +2.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.3 | +5.6 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.3 | +3.0 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -5.8 | -7.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.0 | -7.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -3.9 | -4.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.5 | -0.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | -2.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.1 | -2.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.7 | -2.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.7 | -1.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.7 | -1.3 |
|  | [[Cyclosporin A (drug)]] 0.05 µM |  | -1.5 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger and BTB domain containing 24 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q21 — chr6:109,460,632-109,483,239 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0441, BIF1, PATZ2; previously ZNF450 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; BTB domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [O43167](https://www.uniprot.org/uniprotkb/O43167) (Zinc finger and BTB domain-containing protein 24):

> May be involved in BMP2-induced transcription.

**Summary**, from NCBI Gene [9841](https://www.ncbi.nlm.nih.gov/gene/9841):

> Predicted to enable DNA-binding transcription factor activity and RNA polymerase II cis-regulatory region sequence-specific DNA binding activity. Predicted to be involved in regulation of transcription by RNA polymerase II. Predicted to act upstream of or within hematopoietic progenitor cell differentiation. Predicted to be located in nucleus. Implicated in immunodeficiency-centromeric instability-facial anomalies syndrome 2. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:21143](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21143) · Entrez [9841](https://www.ncbi.nlm.nih.gov/gene/9841) · UniProt [O43167](https://www.uniprot.org/uniprotkb/O43167) · Ensembl [ENSG00000112365](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000112365)

## Data

Gene col 3363: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3363); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3363, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3363]; `tensor/DDL_lfc|DDL_z.npy` [3363]; `embed/gene_vectors.npy` [3363]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3363 or target_col == 3363). Every well: [[ZBTB24 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZBTB24.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
