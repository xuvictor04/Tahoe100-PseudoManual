---
symbol: "POLL"
type: "gene"
col: 9252
ensembl_id: "ENSG00000166169"
name: "DNA polymerase lambda"
location: "10q24.32"
module: 89
arm: "+"
pooled_cpm: 10.94
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 18
n_dd_up_clean: 1
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/089"]
generated_by: "tahoemap"
---

# POLL

*DNA polymerase lambda* — 10q24.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.20× (z +4.3, q 0.011, up in 14 of 48 measured lines) ⚠ cell-cycle shift, explains ~58% of this change. The strongest without an alert is [[Ponatinib (drug)]] 5 µM: 1.25× (z +3.8, q 0.047, up in 5 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (14 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.619× (z -8.0, q 6e-13, down in 27 of 47 measured lines) ⚠ cell-cycle shift, explains ~32% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.671× (z -6.7, q 2e-09, down in 21 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[METTL22]] (+0.77, fdr 7e-06), [[TEFM]] (+0.71, fdr 7e-06), [[ALKBH3]] (+0.71, fdr 7e-06); moves opposite to [[DIAPH1]] (-0.56, fdr 1e-04), [[EPB41L2]] (-0.55, fdr 2e-05).
> It is in [[Module 089]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9252.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | 1.20× | +4.3 | 0.011 | 14/48 (A498, SW480, …) | rises with dose | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | **1.25×** | +3.8 | 0.047 | 5/47 (RKO, KATO III, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.25×** | +3.5 | 0.084 | 14/45 (HOP62, LOX-IMVI, …) | inconsistent across doses | position effect removed |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~70% of this change | 1.22× | +3.3 | 0.14 | 7/45 (AsPC-1, LS 180, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 1.21× | +3.2 | 0.15 | 12/45 (SK-MEL-2, NCI-H2030, …) | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM |  | 1.41× | +3.0 | 0.24 | 3/43 (SW480, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 14 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9252.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.619×** | -8.0 | 6e-13 | 27/47 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.717×** | -7.9 | 1e-12 | 25/47 (NCI-H460, SNU-423, …) | rises with dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.635×** | -7.6 | 5e-12 | 27/47 (Panc 03.27, NCI-H460, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.659×** | -7.0 | 4e-10 | 23/47 (NCI-H460, COLO 205, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **0.650×** | -6.9 | 4e-10 | 13/19 (SW1417, PANC-1, …) | rises with dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.671×** | -6.7 | 2e-09 | 21/45 (SNU-423, H4, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | **0.687×** | -6.3 | 3e-08 | 22/34 (A-172, NCI-H460, …) | rises with dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **0.678×** | -6.2 | 3e-08 | 22/40 (C32, COLO 205, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.787×** | -5.7 | 9e-07 | 20/47 (NCI-H460, HEC-1-A, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.706×** | -5.6 | 1e-06 | 18/46 (NCI-H460, MIA PaCa-2, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.731×** | -5.2 | 9e-06 | 19/47 (SW1417, NCI-H23, …) | all doses, stronger at high dose | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.737×** | -5.1 | 2e-05 | 19/47 (PANC-1, SW 900, …) | two highest doses |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.750×** | -4.8 | 6e-05 | 17/47 (H4, SNU-423, …) | all doses, stronger at high dose | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.778×** | -4.2 | 0.001 | 17/43 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change | **0.797×** | -3.8 | 0.006 | 19/45 (NCI-H460, SW 900, …) | two highest doses |  |
| [[Brivudine (drug)]] 5 µM |  | **0.702×** | -3.1 | 0.063 | 5/48 (NCI-H460, CHP-212, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9252. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 8.84 | 0 | 3 | — | [[Auranofin (drug)]] 5 µM 0.0630× (z -9.3) |
| [[Hs 766T (line)]] | wt | 9.03 | 0 | 2 (2 ⚠) | — | [[Allantoin (drug)]] 0.05 µM 0.0802× (z -12.3) ⚠ transcription drop |
| [[NCI-H460 (line)]] | wt | 13.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.305× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change |
| [[PANC-1 (line)]] | alt | 13.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.329× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[SNU-423 (line)]] | alt | 15.3 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.153× (z -11.4) |
| [[A-172 (line)]] | wt | 11.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.125× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change |
| [[BT-474 (line)]] | alt | 8.00 | 0 | 1 | — | [[Silodosin (drug)]] 5 µM 0.109× (z -9.1) |
| [[C32 (line)]] | wt | 8.61 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0868× (z -10.7) ⚠ toxic; cell-cycle shift, explains ~28% of this change |
| [[COLO 205 (line)]] | alt | 11.9 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.117× (z -9.1) ⚠ toxic; cell-cycle shift, explains ~28% of this change |
| [[HEC-1-A (line)]] | alt | 13.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.256× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[MIA PaCa-2 (line)]] | alt | 11.6 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.160× (z -9.4) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 12.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.169× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[SW48 (line)]] | wt | 11.4 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 0.05 µM 0.0852× (z -8.5) |
| [[SW480 (line)]] | alt | 11.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.317× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.84 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.34 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.84 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.27 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.29 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.33 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.06 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.43 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.14 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 9.02 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.92 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.48 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.67 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.89 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9252), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[METTL22]] | +0.77 | +0.72 / +0.71 | both halves | 7e-06 |  |
| [[TEFM]] | +0.71 | +0.72 / +0.65 | both halves | 7e-06 |  |
| [[ALKBH3]] | +0.71 | +0.69 / +0.67 | both halves | 7e-06 |  |
| [[YJU2B]] | +0.69 | +0.54 / +0.71 | both halves | 1e-05 |  |
| [[SETDB1]] | +0.69 | +0.63 / +0.72 | both halves | 7e-06 |  |
| [[POLR3F]] | +0.68 | +0.64 / +0.67 | both halves | 7e-06 |  |
| [[ALKBH4]] | +0.68 | +0.58 / +0.69 | both halves | 7e-06 |  |
| [[GPATCH3]] | +0.66 | +0.58 / +0.64 | both halves | 8e-06 |  |
| [[ALKBH1]] | +0.65 | +0.57 / +0.67 | both halves | 1e-05 |  |
| [[ANKRD49]] | +0.64 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[MAU2]] | +0.63 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[DNAJC30]] | +0.62 | +0.51 / +0.62 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DIAPH1]] | -0.56 | -0.33 / -0.61 | both halves | 1e-04 |  |
| [[EPB41L2]] | -0.55 | -0.46 / -0.57 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 089]]; 51 genes; every member is in the + arm (projection on the module's main direction 0.769). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-43.7, 7.6); signed map (-9.0, -16.5). **Vector** length 60.2, 8.57% of its response variance represented; |z| ≥ 3 in 850 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | +4.0 | +4.3 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~41% of this change | +3.6 | +3.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +3.6 | +0.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.4 | +3.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | +2.3 | +0.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.8 | +3.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.4 | -0.9 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.3 | +1.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.3 | +0.4 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | -4.2 | -6.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.9 | -5.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | -3.6 | -6.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | -3.6 | -6.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -3.1 | -1.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.8 | -6.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.5 | -2.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.3 | -3.1 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | -1.1 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | DNA polymerase lambda |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q24.32 — chr10:101,578,882-101,588,270 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | DNA polymerases |
| Hallmark sets | DNA_REPAIR |
| Reactome | 3 pathways, smallest: Nonhomologous End-Joining (NHEJ); DNA Double-Strand Break Repair; DNA Repair |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UGP5](https://www.uniprot.org/uniprotkb/Q9UGP5) (DNA polymerase lambda):

> DNA polymerase that functions in several pathways of DNA repair. Involved in base excision repair (BER) responsible for repair of lesions that give rise to abasic (AP) sites in DNA. Also contributes to DNA double-strand break repair by non-homologous end joining and homologous recombination. Has both template-dependent and template-independent (terminal transferase) DNA polymerase activities. Also has a 5'-deoxyribose-5-phosphate lyase (dRP lyase) activity.

**Summary**, from NCBI Gene [27343](https://www.ncbi.nlm.nih.gov/gene/27343):

> This gene encodes a DNA polymerase. DNA polymerases catalyze DNA-template-directed extension of the 3'-end of a DNA strand. This particular polymerase, which is a member of the X family of DNA polymerases, likely plays a role in non-homologous end joining and other DNA repair processes. Alternatively spliced transcript variants have been described. [provided by RefSeq, Mar 2010]

**Accessions** — [HGNC:9184](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9184) · Entrez [27343](https://www.ncbi.nlm.nih.gov/gene/27343) · UniProt [Q9UGP5](https://www.uniprot.org/uniprotkb/Q9UGP5) · Ensembl [ENSG00000166169](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166169)

## Data

Gene col 9252: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9252); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9252, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9252]; `tensor/DDL_lfc|DDL_z.npy` [9252]; `embed/gene_vectors.npy` [9252]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9252 or target_col == 9252). Every well: [[POLL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/POLL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
