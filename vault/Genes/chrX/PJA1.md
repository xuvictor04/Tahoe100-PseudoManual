---
symbol: "PJA1"
type: "gene"
col: 11171
ensembl_id: "ENSG00000181191"
name: "praja ring finger ubiquitin ligase 1"
location: "Xq13.1"
module: 34
arm: "+"
pooled_cpm: 11.97
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 2
n_dd_up_clean: 3
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/034"]
generated_by: "tahoemap"
---

# PJA1

*praja ring finger ubiquitin ligase 1* — Xq13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 1.14× (z +6.2, q 4e-07, up in 9 of 48 measured lines) ⚠ position not correctable. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 1.48× (z +5.5, q 1e-05, up in 21 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.710× (z -6.0, q 1e-06, down in 20 of 45 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (KATO III 0.270×, AsPC-1 0.300×); [[Dinaciclib (drug)]] 5 µM in 1 line (J82 0.134×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (LoVo 0.184×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Penfluridol (drug)]] 5 µM in 1 line (BT-474 0.0947×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LYPD3]] (+0.59, fdr 1e-05), [[PLEK2]] (+0.56, fdr 1e-05), [[GDPD5]] (+0.55, fdr 1e-05); moves opposite to [[NUCKS1]] (-0.46, fdr 1e-04), [[ARID2]] (-0.45, fdr 1e-04), [[MTUS1-DT]] (-0.44, fdr 2e-04).
> It is in [[Module 034]], a single-armed module (Type I hemidesmosome assembly).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[DGKA]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 5 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11171.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.14× | +6.2 | 4e-07 | 9/48 (KATO III, A-172, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.48×** | +5.5 | 1e-05 | 21/48 (PANC-1, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~18% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.49×** | +5.4 | 1e-05 | 17/39 (HT-29, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.40×** | +4.8 | 2e-04 | 17/42 (NCI-H460, HEC-1-A, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~3% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.32×** | +4.7 | 3e-04 | 16/48 (BT-474, SW480, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.33×** | +4.0 | 0.006 | 15/47 (SW1417, PANC-1, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.25×** | +3.9 | 0.009 | 15/48 (SNU-423, Hs 766T, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.26×** | +3.3 | 0.080 | 9/47 (A498, NCI-H2030, …) | inconsistent across doses |  |
| [[Infigratinib (drug)]] 0.05 µM |  | 1.26× | +3.1 | 0.13 | 6/48 (SW480, KATO III, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11171.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (KATO III 0.270×, AsPC-1 0.300×); [[Dinaciclib (drug)]] 5 µM in 1 line (J82 0.134×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (LoVo 0.184×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Penfluridol (drug)]] 5 µM in 1 line (BT-474 0.0947×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.710×** | -6.0 | 1e-06 | 20/45 (KATO III, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Anethole trithione (drug)]] 5 µM |  | **0.779×** | -4.6 | 0.001 | 12/48 (HOP62, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | 0.787× | -3.4 | 0.12 | 13/45 (LoVo, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | 0.639× | -3.3 | 0.12 | 15/43 (PANC-1, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11171. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 11.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.184× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[AsPC-1 (line)]] | alt | 24.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.300× (z -9.2) |
| [[BT-474 (line)]] | alt | 6.08 | 0 | 1 | — | [[Penfluridol (drug)]] 5 µM 0.0947× (z -8.5) |
| [[J82 (line)]] | alt | 9.68 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.134× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change |
| [[KATO III (line)]] | alt | 34.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -12.1) |
| [[A-172 (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.26 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.78 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.94 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.49 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.39 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.63 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.69 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 20.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.85 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.89 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.27 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.73 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.22 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.28 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.90 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.48 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.41 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 6.76 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.08 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 7.80 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.80 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.98 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.33 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.68 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.88 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 17.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11171), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LYPD3]] | +0.59 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[PLEK2]] | +0.56 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[GDPD5]] | +0.55 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[PLEKHG5]] | +0.55 | +0.48 / +0.49 | both halves | 2e-05 |  |
| [[PKP1]] | +0.54 | +0.48 / +0.49 | both halves | 2e-05 |  |
| [[PCDH1]] | +0.54 | +0.44 / +0.50 | both halves | 3e-05 |  |
| [[NGEF]] | +0.53 | +0.49 / +0.46 | both halves | 3e-05 |  |
| [[PRSS3]] | +0.53 | +0.48 / +0.47 | both halves | 2e-05 |  |
| [[FCHSD1]] | +0.52 | +0.44 / +0.51 | both halves | 3e-05 |  |
| [[DENND2C]] | +0.51 | +0.43 / +0.53 | both halves | 3e-05 |  |
| [[PLEKHM1]] | +0.50 | +0.45 / +0.45 | both halves | 3e-05 |  |
| [[CYB5R2]] | +0.50 | +0.41 / +0.51 | both halves | 4e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUCKS1]] | -0.46 | -0.33 / -0.47 | both halves | 1e-04 |  |
| [[ARID2]] | -0.45 | -0.33 / -0.46 | both halves | 1e-04 |  |
| [[MTUS1-DT]] | -0.44 | -0.44 / -0.29 | both halves | 2e-04 |  |
| [[ASH1L]] | -0.43 | -0.37 / -0.44 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DGKA]] | B | DGKA activity raises PJA1's level | lines that do not express DGKA (6) vs lines expressing it (44) | 1.62× lower at baseline in the lines without DGKA | 0.037 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers PJA1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers PJA1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[ESAM]] | C | ESAM activity raises PJA1's level | lines that do not express ESAM (4) vs lines expressing it (46) | 1.64× lower at baseline in the lines without ESAM | 0.088 | ⚠ few lines (4 vs 46); within organs, on part of the lines; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 034]] — Type I hemidesmosome assembly; 137 genes; every member is in the + arm (projection on the module's main direction 0.598). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (11.9, 55.4); signed map (-0.6, 44.8). **Vector** length 61.7, 9.39% of its response variance represented; |z| ≥ 3 in 765 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.1 | +4.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.5 | +3.0 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.3 | +3.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.6 | +2.8 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +2.4 | +4.8 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.1 | +2.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.8 | +1.2 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +1.8 | +2.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.6 | +1.6 |
| fall | [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | -1.8 | -1.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -1.6 | -6.0 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | -1.5 | -1.5 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | -1.5 | +1.6 |
|  | [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | -1.4 | -2.5 |
|  | [[Sulfatinib (drug)]] 5 µM |  | -1.4 | -0.5 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -1.4 | -1.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.3 | +0.7 |

## What is on record

|  |  |
|---|---|
| Name | praja ring finger ubiquitin ligase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq13.1 — chrX:69,160,851-69,165,521 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ11830, RNF70, PRAJA1 |
| Gene groups (HGNC) | Ring finger proteins; RING finger E3 ubiquitin protein ligases |
| Reactome | 3 pathways, smallest: Antigen processing: Ubiquitination & Proteasome degradation; Class I MHC mediated antigen processing & presentation; Adaptive Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NG27](https://www.uniprot.org/uniprotkb/Q8NG27) (E3 ubiquitin-protein ligase Praja-1):

> Has E2-dependent E3 ubiquitin-protein ligase activity. Ubiquitinates MAGED1 antigen leading to its subsequent degradation by proteasome (By similarity). May be involved in protein sorting.

**Summary**, from NCBI Gene [64219](https://www.ncbi.nlm.nih.gov/gene/64219):

> This gene encodes an enzyme that has E2-dependent E3 ubiquitin-protein ligase activity. This enzyme belongs to a class of ubiquitin ligases that include a RING finger motif, and it can interact with the E2 ubiquitin-conjugating enzyme UbcH5B. This gene is located in an area of chromosome X where several X-linked cognitive disability disorders have been associated, and it has also been found as part of a contiguous gene deletion associated with craniofrontonasal syndrome, though a direct link to …

**Accessions** — [HGNC:16648](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16648) · Entrez [64219](https://www.ncbi.nlm.nih.gov/gene/64219) · UniProt [Q8NG27](https://www.uniprot.org/uniprotkb/Q8NG27) · Ensembl [ENSG00000181191](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000181191)

## Data

Gene col 11171: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11171); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11171, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11171]; `tensor/DDL_lfc|DDL_z.npy` [11171]; `embed/gene_vectors.npy` [11171]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11171 or target_col == 11171). Every well: [[PJA1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PJA1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
