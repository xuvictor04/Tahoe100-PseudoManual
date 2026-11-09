---
symbol: "POLR2C"
type: "gene"
col: 2298
ensembl_id: "ENSG00000102978"
name: "RNA polymerase II subunit C"
location: "16q21"
module: 49
arm: "+"
pooled_cpm: 25.54
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 2
n_dd_up_clean: 9
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/049"]
generated_by: "tahoemap"
---

# POLR2C

*RNA polymerase II subunit C* — 16q21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (10 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 1.95× (z +10.3, q 3e-22, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.749× (z -6.3, q 2e-07, down in 26 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Radotinib (drug)]] 0.5 µM in 1 line (CHP-212 0.102×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (A498 0.573×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BRF2]] (+0.72, fdr 7e-06), [[AARS2]] (+0.68, fdr 1e-05), [[MED8]] (+0.65, fdr 1e-05); moves opposite to [[HMGB1]] (-0.54, fdr 4e-05), [[HIVEP1]] (-0.54, fdr 6e-05), [[MEMO1]] (-0.52, fdr 2e-05).
> It is in [[Module 049]], a single-armed module (XBP1(S) activates chaperone genes).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TFIP11]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 11 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2298.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.95×** | +10.3 | 3e-22 | 43/48 (A-427, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.02×** | +10.3 | 3e-22 | 43/48 (SW480, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.83×** | +9.3 | 2e-18 | 43/48 (SW480, NCI-H460, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.62×** | +7.5 | 1e-11 | 34/48 (SW480, A549, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **1.62×** | +7.4 | 1e-11 | 30/42 (MIA PaCa-2, A-172, …) | two highest doses | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.61×** | +7.3 | 2e-11 | 32/47 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.60×** | +7.3 | 2e-11 | 38/48 (A-427, HEC-1-A, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~31% of this change | **1.51×** | +6.4 | 1e-08 | 33/45 (PANC-1, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.48×** | +6.1 | 7e-08 | 31/48 (SW480, A549, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **1.50×** | +6.0 | 1e-07 | 20/33 (MIA PaCa-2, PANC-1, …) | two highest doses | composition shift |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.94×** | +5.4 | 4e-06 | 22/41 (PANC-1, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~81% of this change | **1.26×** | +5.0 | 3e-05 | 27/47 (NCI-H1573, A549, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.34×** | +4.4 | 5e-04 | 25/46 (LOX-IMVI, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.28×** | +3.8 | 0.006 | 18/48 (SW480, A549, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.26×** | +3.6 | 0.010 | 19/48 (NCI-H2030, A549, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.36×** | +3.4 | 0.019 | 12/48 (LOX-IMVI, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.36×** | +3.4 | 0.020 | 11/48 (A-172, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2298.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Radotinib (drug)]] 0.5 µM in 1 line (CHP-212 0.102×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (A498 0.573×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.749×** | -6.3 | 2e-07 | 26/48 (A498, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.760×** | -4.1 | 0.014 | 21/47 (SW 900, HOP62, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, +0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2298. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 27.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.21× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[NCI-H460 (line)]] | wt | 26.3 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.58× (z +9.0) | — |
| [[A498 (line)]] | wt | 52.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.573× (z -8.6) |
| [[CHP-212 (line)]] | wt | 29.8 | 0 | 1 | — | [[Radotinib (drug)]] 0.5 µM 0.102× (z -8.7) |
| [[PANC-1 (line)]] | alt | 17.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.17× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[SW480 (line)]] | alt | 31.5 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.25× (z +9.2) | — |
| [[A-172 (line)]] | wt | 23.0 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 22.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 22.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 37.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 28.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 26.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 26.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 25.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 27.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 39.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 29.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 23.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 29.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2298), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BRF2]] | +0.72 | +0.78 / +0.66 | both halves | 7e-06 | pathway: HALLMARK_DNA_REPAIR; STRING 496 |
| [[AARS2]] | +0.68 | +0.67 / +0.56 | both halves | 1e-05 |  |
| [[MED8]] | +0.65 | +0.64 / +0.53 | both halves | 1e-05 | STRING 952 |
| [[MYG1]] | +0.65 | +0.65 / +0.53 | both halves | 1e-05 |  |
| [[STAM2]] | +0.65 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[ABCF3]] | +0.62 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[MKRN2]] | +0.62 | +0.58 / +0.57 | both halves | 1e-05 |  |
| [[PSMB1]] | +0.62 | +0.61 / +0.52 | both halves | 1e-05 | pathway: HIV Infection |
| [[PSMD3]] | +0.61 | +0.48 / +0.59 | both halves | 2e-05 | pathway: HIV Infection |
| [[YKT6]] | +0.61 | +0.64 / +0.49 | both halves | 1e-05 |  |
| [[DRG2]] | +0.61 | +0.59 / +0.51 | both halves | 1e-05 | STRING 412 |
| [[RINT1]] | +0.60 | +0.58 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HMGB1]] | -0.54 | -0.56 / -0.42 | both halves | 4e-05 |  |
| [[HIVEP1]] | -0.54 | -0.53 / -0.38 | both halves | 6e-05 |  |
| [[MEMO1]] | -0.52 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[IGF2BP3]] | -0.51 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[SINHCAF]] | -0.50 | -0.42 / -0.45 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TFIP11]] | C | TFIP11's natural level weakens POLR2C's drug response | TFIP11's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.65, reverse +0.08; direction not clear | 0.046 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 049]] — XBP1(S) activates chaperone genes; 93 genes; every member is in the + arm (projection on the module's main direction 0.562). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.12; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-41.8, -5.2); signed map (-23.6, -22.2). **Vector** length 85.5, 18.6% of its response variance represented; |z| ≥ 3 in 858 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +5.6 | +10.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +4.9 | +10.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.1 | +9.3 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +3.3 | +5.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.3 | +3.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.9 | +7.3 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.4 | +2.4 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.2 | +3.4 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +2.0 | +2.7 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.7 | -6.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -5.6 | -2.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -5.4 | -1.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.6 | +2.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.3 | +1.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.8 | -2.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.0 | -1.4 |
|  | [[Neratinib (drug)]] 5 µM |  | -1.4 | -0.7 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -1.3 | -2.1 |
|  | [[EX229 (drug)]] 5 µM |  | -1.2 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | RNA polymerase II subunit C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q21 — chr16:57,462,660-57,472,009 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RPB3 |
| Gene groups (HGNC) | RNA polymerase subunits |
| Hallmark sets | DNA_REPAIR |
| Reactome | 75 pathways, smallest: Signaling by FGFR2 IIIa TM; PIWI-interacting RNA (piRNA) biogenesis; Abortive elongation of HIV-1 transcript in the absence of Tat |
| Matched by | ensembl_id |

**Function**, from UniProt [P19387](https://www.uniprot.org/uniprotkb/P19387) (DNA-directed RNA polymerase II subunit RPB3):

> Core component of RNA polymerase II (Pol II), a DNA-dependent RNA polymerase which synthesizes mRNA precursors and many functional non-coding RNAs using the four ribonucleoside triphosphates as substrates.

**Summary**, from NCBI Gene [5432](https://www.ncbi.nlm.nih.gov/gene/5432):

> This gene encodes the third largest subunit of RNA polymerase II, the polymerase responsible for synthesizing messenger RNA in eukaryotes. The product of this gene contains a cysteine rich region and exists as a heterodimer with another polymerase subunit, POLR2J. These two subunits form a core subassembly unit of the polymerase. A pseudogene has been identified on chromosome 21. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:9189](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9189) · Entrez [5432](https://www.ncbi.nlm.nih.gov/gene/5432) · UniProt [P19387](https://www.uniprot.org/uniprotkb/P19387) · Ensembl [ENSG00000102978](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000102978)

## Data

Gene col 2298: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2298); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2298, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2298]; `tensor/DDL_lfc|DDL_z.npy` [2298]; `embed/gene_vectors.npy` [2298]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2298 or target_col == 2298). Every well: [[POLR2C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/POLR2C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
