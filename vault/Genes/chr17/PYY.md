---
symbol: "PYY"
type: "gene"
col: 5170
ensembl_id: "ENSG00000131096"
name: "peptide YY"
location: "17q21.31"
module: 38
arm: "+"
pooled_cpm: 5.29
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 10
n_dd_up_clean: 6
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/038"]
generated_by: "tahoemap"
---

# PYY

*peptide YY* — 17q21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.59× (z +17.9, q 0e+00, up in 36 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.447× (z -8.0, q 1e-12, down in 23 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ISY1-RAB43]] (+0.76, fdr 7e-06), [[SLC9A5]] (+0.73, fdr 7e-06), [[SYCE2]] (+0.71, fdr 7e-06); moves opposite to [[BTBD3]] (-0.64, fdr 7e-06).
> It is in [[Module 038]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ITGA10]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5170.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.59×** | +17.9 | 0e+00 | 36/39 (LOX-IMVI, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.25×** | +8.0 | 4e-13 | 28/45 (SW480, HT-29, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.87×** | +6.0 | 5e-07 | 2/10 (CFPAC-1, NCI-H2347) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.47×** | +5.3 | 1e-05 | 20/41 (NCI-H460, HCT15, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.55×** | +4.1 | 0.004 | 18/40 (LOX-IMVI, HOP62, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.45×** | +3.7 | 0.024 | 8/44 (CFPAC-1, HOP62, …) | inconsistent across doses | position effect removed |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **1.40×** | +3.3 | 0.068 | 13/44 (hTERT-HPNE, NCI-H1573, …) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 5 µM |  | 1.25× | +3.2 | 0.10 | 12/45 (H4, HOP62, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | 1.38× | +3.2 | 0.10 | 5/39 (HepG2/C3A, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | 1.38× | +3.1 | 0.12 | 8/39 (SW480, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5170.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.447×** | -8.0 | 1e-12 | 23/45 (NCI-H23, hTERT-HPNE, …) | two highest doses | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.462×** | -7.6 | 7e-12 | 26/47 (NCI-H23, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.623×** | -4.7 | 5e-04 | 18/35 (NCI-H23, SW480, …) | two highest doses | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.627×** | -4.6 | 5e-04 | 19/45 (LOX-IMVI, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.629×** | -4.6 | 5e-04 | 20/45 (LOX-IMVI, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.627×** | -4.4 | 9e-04 | 18/34 (LOX-IMVI, A498, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.667×** | -4.0 | 0.005 | 18/46 (A498, NCI-H2030, …) | two highest doses | cell-cycle shift (explains ~12% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.708×** | -3.4 | 0.045 | 15/44 (HT-29, C-33 A, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM |  | **0.521×** | -3.4 | 0.047 | 8/33 (LOX-IMVI, HOP62, …) | top dose only | cell-cycle shift (explains ~24% here); noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.721×** | -3.2 | 0.069 | 13/48 (BT-474, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~36% of this change | 0.737× | -3.0 | 0.13 | 16/26 (KATO III, LoVo, …) | all doses, flat | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, -0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5170. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 22.2 | 1 | 3 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.08× (z +9.4) | [[Digitoxin (drug)]] 5 µM 0.108× (z -13.1) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.180× (z -10.0) |
| [[HOP62 (line)]] | alt | 8.23 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.88× (z +9.6) | [[Digitoxin (drug)]] 5 µM 0.139× (z -9.9) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 3.75 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.90× (z +9.7) | [[Harringtonine (drug)]] 0.05 µM 0.108× (z -8.8) |
| [[CFPAC-1 (line)]] | alt | 8.24 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.96× (z +9.1) | [[Digitoxin (drug)]] 5 µM 0.156× (z -8.8) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 10.4 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.25× (z +11.1) | [[Niclosamide (olamine) (drug)]] 5 µM 0.0669× (z -12.3) ⚠ toxic |
| [[PANC-1 (line)]] | alt | 2.87 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.45× (z +10.2) | [[Dinaciclib (drug)]] 0.5 µM 0.127× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 3.80 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.09× (z +9.2) | [[Digitoxin (drug)]] 5 µM 0.0680× (z -12.4) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 8.66 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.134× (z -8.8) |
| [[A498 (line)]] | wt | 10.9 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.202× (z -8.5) ⚠ toxic |
| [[A549 (line)]] | wt | 3.32 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.56× (z +8.5) | — |
| [[hTERT-HPNE (line)]] | wt | 7.56 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0517× (z -9.5) |
| [[KATO III (line)]] | alt | 4.42 | 0 | 1 | — | [[Peretinoin (drug)]] 5 µM 0.0794× (z -8.8) |
| [[NCI-H2030 (line)]] | alt | 7.80 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.103× (z -9.5) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 6.67 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.57 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.83 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.40 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.37 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.77 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.57 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.59 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.95 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.68 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.20 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.17 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.20 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.26 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.06 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.01 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.26 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.84 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.59 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.58 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.47 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.44 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.37 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.65 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.13 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.02 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5170), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ISY1-RAB43]] | +0.76 | +0.68 / +0.76 | both halves | 7e-06 |  |
| [[SLC9A5]] | +0.73 | +0.74 / +0.66 | both halves | 7e-06 |  |
| [[SYCE2]] | +0.71 | +0.73 / +0.64 | both halves | 7e-06 |  |
| [[MASP2]] | +0.71 | +0.69 / +0.64 | both halves | 7e-06 |  |
| [[AZU1]] | +0.71 | +0.71 / +0.63 | both halves | 7e-06 |  |
| [[ARL9]] | +0.70 | +0.73 / +0.59 | both halves | 7e-06 |  |
| [[NUP210L]] | +0.70 | +0.70 / +0.62 | both halves | 7e-06 |  |
| [[PHYHD1]] | +0.69 | +0.59 / +0.71 | both halves | 7e-06 |  |
| [[FNDC7]] | +0.69 | +0.72 / +0.59 | both halves | 7e-06 |  |
| [[TINCR]] | +0.68 | +0.77 / +0.70 | both halves | 7e-06 |  |
| [[CPT1C]] | +0.68 | +0.69 / +0.61 | both halves | 7e-06 |  |
| [[TTLL3]] | +0.67 | +0.57 / +0.71 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BTBD3]] | -0.64 | -0.60 / -0.62 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ITGA10]] | B | ITGA10 activity raises PYY's level | lines that do not express ITGA10 (9) vs lines expressing it (41) | 1.77× lower at baseline in the lines without ITGA10 | 0.048 | ⚠ within organs, on part of the lines; also absent: SLC17A7, ZEB1, BOLA3-DT; maybe low, not absent |
| [[SLC26A4]] | B | SLC26A4 activity raises PYY's level | lines that do not express SLC26A4 (7) vs lines expressing it (43) | 1.61× lower at baseline in the lines without SLC26A4 | 0.087 | ⚠ within organs, on part of the lines; also absent: HES4; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 038]]; 122 genes; every member is in the + arm (projection on the module's main direction 0.786). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (34.2, -18.8); signed map (13.2, 11.6). **Vector** length 79.4, 14.1% of its response variance represented; |z| ≥ 3 in 1,105 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.3 | +17.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.2 | +8.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.5 | +5.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +2.5 | +4.1 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +2.5 | +3.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.3 | +0.9 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.7 | +3.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.6 | +2.1 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -3.7 | -8.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.3 | -7.6 |
|  | [[NG25 (drug)]] 5 µM |  | -3.2 | -3.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.2 | -2.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.0 | -4.0 |
|  | [[Pralsetinib (drug)]] 5 µM |  | -2.5 | -2.1 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.2 | -1.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.9 | -2.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.8 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | peptide YY |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.31 — chr17:43,952,733-44,004,469 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PYY1 |
| Gene groups (HGNC) | Neuropeptides |
| Reactome | 6 pathways, smallest: Peptide ligand-binding receptors; Class A/1 (Rhodopsin-like receptors); G alpha (i) signalling events |
| Matched by | ensembl_id |

**Function**, from UniProt [P10082](https://www.uniprot.org/uniprotkb/P10082) (Peptide YY):

> [Peptide YY]: Ligand for neuropeptide Y receptor type 1 (NPY1R) and neuropeptide Y receptor type 2 (NPY2R). Also binds NPY5R (By similarity). Receptor binding induces adenylate cyclase-inhibiting G protein-coupled receptor signaling, resulting in inhibition of cAMP production. Receptor activation by PYY also leads to an increase of intracellular Ca(2+) levels. This gut peptide inhibits exocrine pancreatic secretion (By similarity). Involved in the regulation of colonic antisecretory tone, and …

**Summary**, from NCBI Gene [5697](https://www.ncbi.nlm.nih.gov/gene/5697):

> This gene encodes a member of the neuropeptide Y (NPY) family of peptides. The encoded preproprotein is proteolytically processed to generate two alternative peptide products that differ in length by three amino acids. These peptides, secreted by endocrine cells in the gut, exhibit different binding affinities for each of the neuropeptide Y receptors. Binding of the encoded peptides to these receptors mediates regulation of pancreatic secretion, gut mobility and energy homeostasis. Rare …

**Accessions** — [HGNC:9748](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9748) · Entrez [5697](https://www.ncbi.nlm.nih.gov/gene/5697) · UniProt [P10082](https://www.uniprot.org/uniprotkb/P10082) · Ensembl [ENSG00000131096](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000131096)

## Data

Gene col 5170: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5170); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5170, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5170]; `tensor/DDL_lfc|DDL_z.npy` [5170]; `embed/gene_vectors.npy` [5170]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5170 or target_col == 5170). Every well: [[PYY — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PYY.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
