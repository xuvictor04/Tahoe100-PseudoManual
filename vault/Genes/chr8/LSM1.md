---
symbol: "LSM1"
type: "gene"
col: 10596
ensembl_id: "ENSG00000175324"
name: "LSM1 homolog, mRNA degradation associated"
location: "8p11.23"
module: 114
arm: "+"
pooled_cpm: 17.34
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 2
n_dd_up_clean: 6
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/114"]
generated_by: "tahoemap"
---

# LSM1

*LSM1 homolog, mRNA degradation associated* — 8p11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (12 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.25× (z +12.0, q 2e-30, up in 29 of 33 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 2.62× (z +6.9, q 7e-10, up in 30 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.771× (z -5.6, q 2e-05, down in 28 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM in 1 line (SW48 0.0641×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COPZ1]] (+0.67, fdr 1e-05), [[PPP6C]] (+0.61, fdr 1e-05), [[TMX2]] (+0.61, fdr 1e-05); moves opposite to [[KHDRBS3]] (-0.57, fdr 3e-05), [[PPP2R2A]] (-0.54, fdr 4e-05), [[METAP1]] (-0.54, fdr 4e-05).
> It is in [[Module 114]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 12 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10596.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.25×** | +12.0 | 2e-30 | 29/33 (LoVo, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **2.14×** | +11.7 | 2e-29 | 31/42 (SW480, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **1.75×** | +8.6 | 2e-15 | 30/46 (LOX-IMVI, NCI-H1573, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~77% of this change | **1.39×** | +7.1 | 2e-10 | 32/47 (LOX-IMVI, HCT15, …) | rises with dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.62×** | +6.9 | 7e-10 | 30/47 (SW480, HEC-1-A, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.56×** | +6.8 | 9e-10 | 26/47 (LOX-IMVI, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.37×** | +6.8 | 9e-10 | 32/47 (SW480, HOP62, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.56×** | +6.6 | 3e-09 | 26/47 (LOX-IMVI, SW480, …) | top dose only | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.50×** | +6.2 | 3e-08 | 28/48 (NCI-H1573, SW480, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.48×** | +6.0 | 8e-08 | 28/46 (LOX-IMVI, PANC-1, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.49×** | +5.9 | 2e-07 | 23/43 (CFPAC-1, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.41×** | +5.3 | 5e-06 | 19/46 (LOX-IMVI, A-172, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **1.41×** | +4.9 | 4e-05 | 17/36 (Hs 766T, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~59% of this change | **1.34×** | +4.5 | 3e-04 | 20/45 (HOP62, Panc 03.27, …) | inconsistent across doses | low cells (technical?) |
| [[PH-797804 (drug)]] 5 µM |  | **1.76×** | +4.1 | 0.002 | 17/45 (SW480, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.30×** | +3.9 | 0.004 | 12/47 (HOP62, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10596.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM in 1 line (SW48 0.0641×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.771×** | -5.6 | 2e-05 | 28/48 (HS-578T, HCT15, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.717×** | -5.1 | 1e-04 | 19/46 (NCI-H460, CHP-212, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, +0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10596. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 13.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.30× (z +11.6) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 17.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 5.16× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | — |
| [[SHP-77 (line)]] | alt | 31.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.45× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[SW480 (line)]] | alt | 20.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.19× (z +11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[A-172 (line)]] | wt | 20.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.08× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[HS-578T (line)]] | alt | 23.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.66× (z +9.4) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 18.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.08× (z +12.8) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 13.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.49× (z +9.2) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 17.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.02× (z +9.4) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 23.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.71× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[SW48 (line)]] | wt | 16.2 | 0 | 1 | — | [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM 0.0641× (z -10.0) |
| [[A-427 (line)]] | wt | 20.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 29.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 16.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.06 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 19.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.00 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 21.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 19.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 9.54 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 22.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.30 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.74 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.12 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10596), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COPZ1]] | +0.67 | +0.66 / +0.57 | both halves | 1e-05 |  |
| [[PPP6C]] | +0.61 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[TMX2]] | +0.61 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[DNAJB14]] | +0.59 | +0.58 / +0.48 | both halves | 2e-05 |  |
| [[GOSR1]] | +0.59 | +0.54 / +0.66 | both halves | 1e-05 |  |
| [[ZBTB8OS]] | +0.59 | +0.58 / +0.43 | both halves | 3e-05 |  |
| [[ALKBH1]] | +0.59 | +0.67 / +0.47 | both halves | 2e-05 |  |
| [[TRIM4]] | +0.58 | +0.67 / +0.48 | both halves | 2e-05 |  |
| [[GPN2]] | +0.58 | +0.53 / +0.44 | both halves | 3e-05 |  |
| [[SLC35B1]] | +0.58 | +0.48 / +0.64 | both halves | 2e-05 |  |
| [[KRIT1]] | +0.58 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[TM9SF4]] | +0.57 | +0.56 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KHDRBS3]] | -0.57 | -0.46 / -0.53 | both halves | 3e-05 |  |
| [[PPP2R2A]] | -0.54 | -0.42 / -0.58 | both halves | 4e-05 |  |
| [[METAP1]] | -0.54 | -0.53 / -0.40 | both halves | 4e-05 |  |
| [[IL17RD]] | -0.53 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[INPP5F]] | -0.52 | -0.53 / -0.35 | both halves | 1e-04 |  |
| [[AFDN]] | -0.52 | -0.47 / -0.46 | both halves | 3e-05 |  |
| [[HPSE]] | -0.50 | -0.40 / -0.42 | both halves | 5e-05 |  |
| [[LTA4H]] | -0.49 | -0.51 / -0.34 | both halves | 1e-04 |  |
| [[GTDC1]] | -0.49 | -0.38 / -0.40 | both halves | 6e-05 |  |
| [[SLC29A1]] | -0.48 | -0.39 / -0.36 | both halves | 1e-04 |  |
| [[RYBP]] | -0.48 | -0.36 / -0.48 | both halves | 1e-04 |  |
| [[STRN]] | -0.47 | -0.54 / -0.25 | both halves | 4e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 114]]; 42 genes; every member is in the + arm (projection on the module's main direction 0.608). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.38; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-25.9, -10.3); signed map (-6.2, -12.0). **Vector** length 59.0, 9.68% of its response variance represented; |z| ≥ 3 in 701 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +3.6 | +6.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.5 | +6.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~77% of this change | +2.3 | +7.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +2.2 | +6.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.0 | +4.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.9 | +2.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.6 | +5.3 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +1.2 | +0.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.1 | +1.7 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -4.4 | -5.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -3.0 | -5.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.6 | -2.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -2.2 | +1.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.1 | -1.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.4 | -0.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.1 | -0.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.0 | -1.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.0 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | LSM1 homolog, mRNA degradation associated |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p11.23 — chr8:38,163,335-38,176,730 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CASM, YJL124C |
| Gene groups (HGNC) | LSm proteins |
| Hallmark sets | UNFOLDED_PROTEIN_RESPONSE |
| Reactome | 3 pathways, smallest: mRNA decay by 5' to 3' exoribonuclease; Deadenylation-dependent mRNA decay; Metabolism of RNA |
| Matched by | ensembl_id |

**Function**, from UniProt [O15116](https://www.uniprot.org/uniprotkb/O15116) (U6 snRNA-associated Sm-like protein LSm1):

> Plays a role in the degradation of histone mRNAs, the only eukaryotic mRNAs that are not polyadenylated. Probably also part of an LSm subunits-containing complex involved in the general process of mRNA degradation (By similarity).

**Summary**, from NCBI Gene [27257](https://www.ncbi.nlm.nih.gov/gene/27257):

> This gene encodes a member of the LSm family of RNA-binding proteins. LSm proteins form stable heteromers that bind specifically to the 3'-terminal oligo(U) tract of U6 snRNA and may play a role in pre-mRNA splicing by mediating U4/U6 snRNP formation. Increased expression of this gene may play a role in cellular transformation and the progression of several malignancies including lung cancer, mesothelioma and breast cancer. Alternatively spliced transcript variants have been observed for this …

**Accessions** — [HGNC:20472](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20472) · Entrez [27257](https://www.ncbi.nlm.nih.gov/gene/27257) · UniProt [O15116](https://www.uniprot.org/uniprotkb/O15116) · Ensembl [ENSG00000175324](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000175324)

## Data

Gene col 10596: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10596); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10596, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10596]; `tensor/DDL_lfc|DDL_z.npy` [10596]; `embed/gene_vectors.npy` [10596]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10596 or target_col == 10596). Every well: [[LSM1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LSM1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
