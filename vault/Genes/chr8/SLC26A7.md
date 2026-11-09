---
symbol: "SLC26A7"
type: "gene"
col: 7205
ensembl_id: "ENSG00000147606"
name: "solute carrier family 26 member 7"
location: "8q21.3"
module: 26
arm: "+"
pooled_cpm: 3.23
n_lines_expressing: 46
n_dd_up: 30
n_dd_down: 0
n_dd_up_clean: 22
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 4
direction_downstream: 1
tags: ["gene", "module/026"]
generated_by: "tahoemap"
---

# SLC26A7

*solute carrier family 26 member 7* — 8q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.13× (z +15.4, q 0e+00, up in 27 of 29 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Fulvestrant (drug)]] 0.5 µM in 1 line (C32 0.0602×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ST8SIA5]] (+0.80, fdr 7e-06), [[FRZB]] (+0.79, fdr 7e-06), [[LINC02641]] (+0.79, fdr 7e-06).
> It sits in the **+** arm of [[Module 026]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[LINC02398]] → it (grade B ⚠); 1 goes from it, the strongest it → [[LRRC69]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 8 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7205.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.13×** | +15.4 | 0e+00 | 27/29 (A498, HS-578T, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **6.20×** | +13.5 | 6e-39 | 22/29 (HS-578T, SW480, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.87×** | +11.4 | 6e-28 | 27/35 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **4.40×** | +10.9 | 1e-25 | 26/32 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **2.63×** | +10.5 | 1e-23 | 26/43 (HS-578T, HOP62, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.89×** | +8.1 | 4e-14 | 22/31 (NCI-H2347, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.81×** | +7.9 | 2e-13 | 25/36 (LoVo, A-427, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **2.77×** | +7.8 | 4e-13 | 26/43 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.80×** | +7.6 | 2e-12 | 0/4 | all doses, flat | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.84×** | +7.4 | 8e-12 | 4/7 (NCI-H460, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~5% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.77×** | +6.2 | 4e-08 | 14/43 (NCI-H1573, NCI-H460, …) | rises with dose | low cells (technical?) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.22×** | +6.1 | 5e-08 | 12/27 (COLO 205, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.16×** | +5.9 | 2e-07 | 5/15 (NCI-H460, SW 900, …) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.20×** | +5.8 | 3e-07 | 11/19 (HOP62, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.97×** | +5.2 | 7e-06 | 18/43 (COLO 205, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **2.00×** | +5.1 | 1e-05 | 14/31 (A498, HOP62, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.92×** | +5.0 | 2e-05 | 14/40 (A498, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **3.14×** | +4.6 | 1e-04 | 13/37 (PANC-1, HOP62, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **1.79×** | +4.4 | 3e-04 | 15/41 (NCI-H23, A498, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.76×** | +4.0 | 0.002 | 13/40 (SHP-77, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.73×** | +3.9 | 0.003 | 11/42 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~21% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7205.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Fulvestrant (drug)]] 0.5 µM in 1 line (C32 0.0602×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | 0.439× | -3.3 | 0.39 | 9/23 (NCI-H1573, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | 0.663× | -3.2 | 0.39 | 8/43 (SW48, NCI-H1573, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 5 µM |  | 0.759× | -3.0 | 0.39 | 4/43 (H4, LOX-IMVI, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.37 per unit of S-phase module lfc, -0.53 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7205. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 2.78 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 16.0× (z +9.8) | — |
| [[A498 (line)]] | wt | 2.75 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.55× (z +9.9) | — |
| [[C32 (line)]] | wt | 8.48 | 0 | 1 | — | [[Fulvestrant (drug)]] 0.5 µM 0.0602× (z -8.5) |
| [[A-172 (line)]] | wt | 0.775 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.78 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.08 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.65 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.839 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.58 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.04 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.55 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.83 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.55 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.89 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.41 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.15 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.00 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.791 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.22 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.30 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.666 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 9.06 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.79 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.26 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.71 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.88 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.94 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.905 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.57 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.71 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.82 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.90 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.04 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.39 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.614 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.10 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.09 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7205), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ST8SIA5]] | +0.80 | +0.79 / +0.68 | both halves | 7e-06 |  |
| [[FRZB]] | +0.79 | +0.75 / +0.68 | both halves | 7e-06 |  |
| [[LINC02641]] | +0.79 | +0.72 / +0.65 | both halves | 7e-06 |  |
| [[BAALC-AS1]] | +0.79 | +0.76 / +0.58 | both halves | 7e-06 |  |
| [[MGAM]] | +0.78 | +0.77 / +0.68 | both halves | 7e-06 |  |
| [[HSD17B3]] | +0.77 | +0.77 / +0.59 | both halves | 7e-06 |  |
| [[MCF2]] | +0.76 | +0.77 / +0.54 | both halves | 1e-05 |  |
| [[CASS4]] | +0.75 | +0.79 / +0.54 | both halves | 1e-05 |  |
| [[DCAF4L1]] | +0.75 | +0.77 / +0.63 | both halves | 7e-06 |  |
| [[PDC-AS1]] | +0.75 | +0.76 / +0.53 | both halves | 1e-05 |  |
| [[TPTE2]] | +0.74 | +0.69 / +0.64 | both halves | 7e-06 |  |
| [[CCDC30]] | +0.74 | +0.77 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02398]] | B | LINC02398 activity raises SLC26A7's level | lines that do not express LINC02398 (13) vs lines expressing it (37) | 2.18× lower at baseline in the lines without LINC02398 | 0.008 | ⚠ within organs, on part of the lines; also absent: ANKRD7, KCNMB2, IGSF11; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers SLC26A7's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.2% of all compounds | 0.047 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ANKRD7]] | B | ANKRD7 activity raises SLC26A7's level | lines that do not express ANKRD7 (11) vs lines expressing it (39) | 1.72× lower at baseline in the lines without ANKRD7 | 0.058 | ⚠ within organs, on part of the lines; also absent: PCDH15, LINC02398, ABCA12; maybe low, not absent |
| [[ST8SIA5]] | B | ST8SIA5 activity raises SLC26A7's level | lines that do not express ST8SIA5 (5) vs lines expressing it (45) | 1.93× lower at baseline in the lines without ST8SIA5 | 0.066 | ⚠ within organs, on part of the lines; also absent: FBLN7, CLEC2D, IMPG2; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LRRC69]] | C | SLC26A7 activity raises LRRC69's level | lines that do not express SLC26A7 (4) vs lines expressing it (46) | 2.51× lower at baseline in the lines without SLC26A7 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 026]]; 163 genes; this gene is in the **+** arm (projection on the module's main direction 0.779). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (13.3, 16.7); signed map (22.5, 0.9). **Vector** length 64.6, 10.6% of its response variance represented; |z| ≥ 3 in 1,074 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +5.0 | +7.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.2 | +10.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.1 | +7.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.0 | +7.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.9 | +13.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.5 | +2.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.1 | +5.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.1 | +5.1 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.9 | +0.1 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.8 | +4.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.2 | +3.9 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.1 | +1.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.1 | +1.4 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -1.7 | -1.0 |
|  | [[Fumaric acid (drug)]] 5 µM |  | -1.5 | -1.3 |
|  | [[Tirabrutinib (drug)]] 5 µM |  | -1.5 | -2.1 |
|  | [[Retinoic acid (drug)]] 5 µM |  | -1.5 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 26 member 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q21.3 — chr8:91,209,494-91,398,155 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SUT2 |
| Gene groups (HGNC) | Solute carrier family 26 |
| Reactome | 4 pathways, smallest: Inorganic anion exchange by SLC26 transporters; SLC-mediated transport of inorganic anions; SLC-mediated transmembrane transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TE54](https://www.uniprot.org/uniprotkb/Q8TE54) (Anion exchange transporter):

> Acts as an anion channel mediating the transport of chloride, sulfate and oxalate ions. Mediates the transport of bromide, iodide, nitrate, gluconate, thiocyanate and bicarbonate ions (By similarity). Its permeability towards bicarbonate is weak and increases when pH is above 7 (By similarity). Mediates thiocyanate transport in retinal pigment epithelium cells (By similarity). Mediates iodide transport in the thyroid gland, playing an important role in the synthesis of thyroid hormones and the …

**Summary**, from NCBI Gene [115111](https://www.ncbi.nlm.nih.gov/gene/115111):

> This gene is one member of a family of sulfate/anion transporter genes. Family members are well conserved in gene structure and protein length yet have markedly different tissue expression patterns. This gene has abundant and specific expression in the kidney. Alternatively spliced transcript variants that encode different isoforms have been described. [provided by RefSeq, Aug 2013]

**Accessions** — [HGNC:14467](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14467) · Entrez [115111](https://www.ncbi.nlm.nih.gov/gene/115111) · UniProt [Q8TE54](https://www.uniprot.org/uniprotkb/Q8TE54) · Ensembl [ENSG00000147606](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000147606)

## Data

Gene col 7205: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7205); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7205, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7205]; `tensor/DDL_lfc|DDL_z.npy` [7205]; `embed/gene_vectors.npy` [7205]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7205 or target_col == 7205). Every well: [[SLC26A7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC26A7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
