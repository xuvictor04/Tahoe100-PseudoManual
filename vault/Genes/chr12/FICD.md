---
symbol: "FICD"
type: "gene"
col: 12709
ensembl_id: "ENSG00000198855"
name: "FIC domain protein adenylyltransferase"
location: "12q23.3"
module: 49
arm: "+"
pooled_cpm: 5.91
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 0
n_dd_up_clean: 10
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/049"]
generated_by: "tahoemap"
---

# FICD

*FIC domain protein adenylyltransferase* — 12q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 2.44× (z +9.0, q 9e-17, up in 21 of 30 measured lines) ⚠ toxic. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 2.12× (z +7.9, q 7e-13, up in 27 of 45 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 6 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 2 lines (KATO III 0.121×, NCI-H1573 0.229×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (NCI-H1573 0.0854×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~11% of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (NCI-H1573 0.149×; ⚠ toxic); [[Hesperidin (drug)]] 5 µM in 1 line (NCI-H1792 0.0597×); [[Fluvoxamine (maleate) (drug)]] 0.05 µM in 1 line (Hs 766T 0.0789×); [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM in 1 line (SW 900 0.101×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ALG2]] (+0.77, fdr 7e-06), [[SRP19]] (+0.68, fdr 7e-06), [[SELENOS]] (+0.68, fdr 1e-05); moves opposite to [[YWHAQ]] (-0.49, fdr 2e-05), [[LAPTM4B]] (-0.48, fdr 7e-05), [[RBBP7]] (-0.46, fdr 4e-05).
> It is in [[Module 049]], a single-armed module (XBP1(S) activates chaperone genes).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → [[SLC33A1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12709.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.44×** | +9.0 | 9e-17 | 21/30 (NCI-H1573, HOP62, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.12×** | +7.9 | 7e-13 | 27/45 (A498, SW480, …) | two highest doses | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.02×** | +7.4 | 3e-11 | 21/38 (NCI-H1573, A-172, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.97×** | +7.1 | 1e-10 | 27/44 (MIA PaCa-2, A-172, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM |  | **1.83×** | +6.4 | 2e-08 | 24/46 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.69×** | +5.5 | 3e-06 | 21/47 (HOP62, SW480, …) | two highest doses | cell-cycle shift (explains ~2% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.15× | +5.2 | 2e-05 | 11/48 (NCI-H460, NCI-H1573, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.52×** | +4.2 | 0.002 | 11/43 (PANC-1, A498, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.35×** | +4.2 | 0.002 | 14/37 (SNU-423, A-172, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.45×** | +3.9 | 0.006 | 6/37 (NCI-H2030, HS-578T, …) | inconsistent across doses | low cells (technical?) |
| [[Lipoic acid (drug)]] 5 µM |  | **1.33×** | +3.6 | 0.015 | 7/48 (PANC-1, A498, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.41×** | +3.6 | 0.015 | 9/31 (HCT15, KATO III, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.37×** | +3.3 | 0.039 | 15/46 (NCI-H1573, H4, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **1.37×** | +3.3 | 0.042 | 5/46 (HOP62, KATO III, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12709.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 6 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 2 lines (KATO III 0.121×, NCI-H1573 0.229×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (NCI-H1573 0.0854×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~11% of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (NCI-H1573 0.149×; ⚠ toxic); [[Hesperidin (drug)]] 5 µM in 1 line (NCI-H1792 0.0597×); [[Fluvoxamine (maleate) (drug)]] 0.05 µM in 1 line (Hs 766T 0.0789×); [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM in 1 line (SW 900 0.101×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | 0.728× | -3.2 | 0.61 | 11/43 (NCI-H2030, RPMI-7951, …) | top dose only |  |
| [[Pentamidine (isethionate) (drug)]] 5 µM |  | 0.774× | -3.1 | 0.61 | 10/47 (MIA PaCa-2, LoVo, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12709. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 20.4 | 1 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 6.34× (z +12.0) | [[Dinaciclib (drug)]] 0.05 µM 0.0854× (z -14.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~11% of this change |
| [[Hs 766T (line)]] | wt | 4.42 | 0 | 1 | — | [[Fluvoxamine (maleate) (drug)]] 0.05 µM 0.0789× (z -8.7) |
| [[KATO III (line)]] | alt | 10.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.121× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1792 (line)]] | alt | 5.42 | 0 | 1 | — | [[Hesperidin (drug)]] 5 µM 0.0597× (z -10.0) |
| [[PANC-1 (line)]] | alt | 6.86 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.0918× (z -9.8) ⚠ toxic |
| [[SNU-423 (line)]] | alt | 3.36 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.6× (z +11.8) | — |
| [[SW 900 (line)]] | alt | 7.17 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.101× (z -8.5) |
| [[SW1417 (line)]] | alt | 8.52 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0965× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 8.02 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 5.38 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.67 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.00 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.03 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.39 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.75 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.56 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.86 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.89 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.10 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.51 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.79 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.43 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.24 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.86 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.51 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.32 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.18 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.74 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.88 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.45 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.87 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.68 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.74 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.58 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.03 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.97 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.20 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.00 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.05 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.92 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.45 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.89 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.23 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.46 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.13 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12709), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ALG2]] | +0.77 | +0.80 / +0.73 | both halves | 7e-06 |  |
| [[SRP19]] | +0.68 | +0.65 / +0.71 | both halves | 7e-06 |  |
| [[SELENOS]] | +0.68 | +0.56 / +0.69 | both halves | 1e-05 |  |
| [[SLC33A1]] | +0.68 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[RWDD2A]] | +0.66 | +0.79 / +0.56 | both halves | 1e-05 |  |
| [[SLC35B1]] | +0.64 | +0.74 / +0.54 | both halves | 1e-05 |  |
| [[DNAJB9]] | +0.64 | +0.57 / +0.63 | both halves | 1e-05 |  |
| [[SEC61B]] | +0.62 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[SEC11C]] | +0.62 | +0.72 / +0.60 | both halves | 7e-06 |  |
| [[XBP1]] | +0.58 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[DERL2]] | +0.58 | +0.47 / +0.54 | both halves | 2e-05 |  |
| [[GOLGA5]] | +0.58 | +0.41 / +0.63 | both halves | 4e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[YWHAQ]] | -0.49 | -0.48 / -0.46 | both halves | 2e-05 |  |
| [[LAPTM4B]] | -0.48 | -0.37 / -0.44 | both halves | 7e-05 |  |
| [[RBBP7]] | -0.46 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[APP]] | -0.45 | -0.44 / -0.41 | both halves | 4e-05 |  |
| [[LAMB1]] | -0.43 | -0.39 / -0.41 | both halves | 5e-05 |  |
| [[CERS6]] | -0.43 | -0.42 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC33A1]] | C | FICD's natural level strengthens SLC33A1's drug response | FICD's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.62, reverse -0.08; direction not clear | 0.082 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 049]] — XBP1(S) activates chaperone genes; 93 genes; every member is in the + arm (projection on the module's main direction 0.603). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.12; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.6, -38.0); signed map (-55.2, 13.7). **Vector** length 71.5, 12.4% of its response variance represented; |z| ≥ 3 in 862 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Cotranslational targeting of proteins to the endoplasmic reticulum* (reactome, mean cos +0.51 to 8); *unfolded protein response* (hallmark, mean cos +0.51 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +5.1 | +7.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.4 | +7.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.1 | +9.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +2.5 | +3.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.0 | +1.8 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.7 | +2.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.7 | +1.9 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.6 | +1.8 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -1.9 | -1.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.6 | -1.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -1.6 | -2.6 |
|  | [[Berberine (chloride hydrate) (drug)]] 5 µM |  | -1.6 | -2.7 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -1.5 | -1.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.4 | -1.6 |
|  | [[Busulfan (drug)]] 5 µM |  | -1.3 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | FIC domain protein adenylyltransferase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q23.3 — chr12:108,515,277-108,525,837 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HYPE, HIP13 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BVA6](https://www.uniprot.org/uniprotkb/Q9BVA6) (Protein adenylyltransferase FICD):

> Protein that can both mediate the addition of adenosine 5'-monophosphate (AMP) to specific residues of target proteins (AMPylation), and the removal of the same modification from target proteins (de-AMPylation), depending on the context (By similarity). The side chain of Glu-231 determines which of the two opposing activities (AMPylase or de-AMPylase) will take place. Acts as a key regulator of the ERN1/IRE1-mediated unfolded protein response (UPR) by mediating AMPylation or de-AMPylation of …

**Summary**, from NCBI Gene [11153](https://www.ncbi.nlm.nih.gov/gene/11153):

> Enables several functions, including AMPylase activity; ATP binding activity; and Hsp70 protein binding activity. Involved in protein adenylylation; regulation of IRE1-mediated unfolded protein response; and response to endoplasmic reticulum stress. Located in endoplasmic reticulum membrane. Implicated in hereditary spastic paraplegia 92. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:18416](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18416) · Entrez [11153](https://www.ncbi.nlm.nih.gov/gene/11153) · UniProt [Q9BVA6](https://www.uniprot.org/uniprotkb/Q9BVA6) · Ensembl [ENSG00000198855](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198855)

## Data

Gene col 12709: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12709); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12709, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12709]; `tensor/DDL_lfc|DDL_z.npy` [12709]; `embed/gene_vectors.npy` [12709]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12709 or target_col == 12709). Every well: [[FICD — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FICD.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
