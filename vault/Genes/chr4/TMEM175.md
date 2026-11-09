---
symbol: "TMEM175"
type: "gene"
col: 4808
ensembl_id: "ENSG00000127419"
name: "transmembrane protein 175"
location: "4p16.3"
module: 209
arm: "+"
pooled_cpm: 3.79
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 5
n_dd_up_clean: 14
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/209"]
generated_by: "tahoemap"
---

# TMEM175

*transmembrane protein 175* — 4p16.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 5.21× (z +19.0, q 0e+00, up in 46 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.607× (z -5.8, q 3e-06, down in 15 of 47 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[VPS16]] (+0.69, fdr 7e-06), [[BAD]] (+0.60, fdr 3e-05), [[C19orf47]] (+0.60, fdr 1e-05); moves opposite to [[GNAL]] (-0.51, fdr 1e-04), [[TXK]] (-0.49, fdr 0.002, ⚠ one half only (not replicated)), [[PRKCE]] (-0.49, fdr 2e-04), [[DNAJA1]] (-0.47, fdr 1e-04).
> It is in [[Module 209]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 4 with an alert ⚠. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4808.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **5.21×** | +19.0 | 0e+00 | 46/47 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **4.71×** | +17.3 | 0e+00 | 44/46 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Belinostat (drug)]] 5 µM |  | **4.35×** | +16.9 | 0e+00 | 44/47 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.64×** | +10.3 | 8e-23 | 5/9 (A498, HOP62, …) | all doses, flat | cell-cycle shift (explains ~11% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.73×** | +8.9 | 6e-17 | 23/37 (A498, SW480, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.20×** | +8.7 | 2e-16 | 3/7 (CFPAC-1, A498, …) | all doses, flat | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.06×** | +8.3 | 9e-15 | 9/20 (NCI-H2347, J82, …) | all doses, flat | cell-cycle shift (explains ~18% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.65×** | +8.2 | 2e-14 | 21/38 (J82, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.95×** | +7.4 | 1e-11 | 12/23 (SW480, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.76×** | +6.3 | 2e-08 | 18/47 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.74×** | +6.1 | 6e-08 | 19/45 (SNU-423, RKO, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.72×** | +6.0 | 9e-08 | 14/32 (A498, SW480, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.49×** | +4.6 | 2e-04 | 5/47 (NCI-H2347, SNU-423, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.49×** | +4.5 | 2e-04 | 8/43 (HEC-1-A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.41×** | +3.9 | 0.003 | 8/46 (NCI-H460, SW480, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.90×** | +3.9 | 0.004 | 6/43 (HT-29, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.35×** | +3.3 | 0.034 | 7/39 (LoVo, HOP62, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.68×** | +3.1 | 0.058 | 8/40 (LoVo, A-427, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4808.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.607×** | -5.8 | 3e-06 | 15/47 (AsPC-1, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.674×** | -4.6 | 0.001 | 14/30 (HOP62, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.688×** | -4.2 | 0.005 | 11/45 (HCT15, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.717×** | -3.8 | 0.024 | 12/43 (HS-578T, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cyclosporin A (drug)]] 0.05 µM |  | **0.743×** | -3.4 | 0.086 | 8/47 (CHP-212, LOX-IMVI, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.29 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4808. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 3.71 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0788× (z -9.6) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 0.05 µM 0.0827× (z -8.7) |
| [[SW480 (line)]] | alt | 3.74 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 7.20× (z +9.2) | — |
| [[A-172 (line)]] | wt | 6.16 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.132× (z -8.7) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HT-29 (line)]] | alt | 5.19 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.0959× (z -8.5) |
| [[NCI-H23 (line)]] | alt | 4.42 | 0 | 1 | — | [[Simotinib (drug)]] 0.05 µM 0.0743× (z -8.7) |
| [[A-427 (line)]] | wt | 4.81 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.44 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.47 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.58 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.10 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.48 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.02 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.81 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.48 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.18 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.64 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.05 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.04 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.75 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.80 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.76 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.22 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.95 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.53 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.43 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.75 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.40 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.25 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.84 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.10 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.68 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.13 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.30 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.69 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.09 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.83 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.97 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.75 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.24 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.07 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4808), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VPS16]] | +0.69 | +0.60 / +0.64 | both halves | 7e-06 | **novel candidate** |
| [[BAD]] | +0.60 | +0.45 / +0.44 | both halves | 3e-05 |  |
| [[C19orf47]] | +0.60 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[ZZEF1]] | +0.55 | +0.55 / +0.48 | both halves | 2e-05 |  |
| [[HARS2]] | +0.55 | +0.44 / +0.45 | both halves | 3e-05 |  |
| [[TBC1D13]] | +0.54 | +0.40 / +0.39 | both halves | 5e-05 |  |
| [[PXMP4]] | +0.54 | +0.34 / +0.52 | both halves | 1e-04 |  |
| [[MMUT]] | +0.54 | +0.48 / +0.38 | both halves | 6e-05 |  |
| [[ZNF18]] | +0.53 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[C1orf50]] | +0.53 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[ASCC2]] | +0.53 | +0.43 / +0.46 | both halves | 3e-05 |  |
| [[C6orf89]] | +0.53 | +0.48 / +0.53 | both halves | 2e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNAL]] | -0.51 | -0.33 / -0.43 | both halves | 1e-04 |  |
| [[TXK]] | -0.49 | -0.13 / -0.51 | ⚠ one half (not replicated) | 0.002 |  |
| [[PRKCE]] | -0.49 | -0.38 / -0.31 | both halves | 2e-04 |  |
| [[DNAJA1]] | -0.47 | -0.33 / -0.45 | both halves | 1e-04 |  |
| [[HSPH1]] | -0.47 | -0.40 / -0.43 | both halves | 5e-05 |  |
| [[TXLNG]] | -0.46 | -0.43 / -0.36 | both halves | 1e-04 |  |
| [[SLIT2]] | -0.45 | -0.22 / -0.37 | both halves | 6e-04 |  |
| [[OR51B5]] | -0.45 | -0.15 / -0.41 | ⚠ not reproduced | 0.001 |  |
| [[LINC01399]] | -0.45 | -0.29 / -0.49 | both halves | 3e-04 |  |
| [[STAU2]] | -0.45 | -0.39 / -0.25 | both halves | 4e-04 |  |
| [[PARD6G-AS1]] | -0.44 | -0.15 / -0.47 | ⚠ not reproduced | 0.001 |  |
| [[AHCYL2]] | -0.44 | -0.43 / -0.25 | both halves | 4e-04 |  |
| [[GALNT14]] | -0.43 | -0.45 / -0.27 | both halves | 3e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 209]]; 13 genes; every member is in the + arm (projection on the module's main direction 0.713). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-33.5, -4.6); signed map (-14.0, -24.0). **Vector** length 44.2, 4.79% of its response variance represented; |z| ≥ 3 in 1,039 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.3 | +8.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.3 | +3.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.0 | +8.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.9 | +10.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.8 | +17.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.2 | +1.8 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +1.3 | +1.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.3 | +0.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.0 | +1.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.0 | +2.0 |
| fall | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | -2.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.8 | -0.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.7 | -3.0 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.7 | -2.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | -0.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.3 | -0.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.2 | -1.6 |
|  | [[EX229 (drug)]] 5 µM |  | -1.1 | -1.3 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.1 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 175 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p16.3 — chr4:932,387-958,656 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC4618 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BSA9](https://www.uniprot.org/uniprotkb/Q9BSA9) (Endosomal/lysosomal proton channel TMEM175):

> Proton-activated proton channel that catalyzes proton efflux from endosomes and lysosomes to maintain a steady-state pH. Activated at low pH (under pH 4.6) by luminal side protons: selectively mediates lysosomal proton release from lysosomes, eliciting a proton leak that balances V-ATPase activity to maintain pH homeostasis. Regulation of lumenal pH stability is required for autophagosome-lysosome fusion. Also acts as a potassium channel at higher pH, regulating potassium conductance in …

**Summary**, from NCBI Gene [84286](https://www.ncbi.nlm.nih.gov/gene/84286):

> Enables arachidonate binding activity; potassium ion leak channel activity; and proton channel activity. Involved in monoatomic cation transmembrane transport and regulation of intracellular pH. Located in endosome membrane and lysosome. Is active in lysosomal membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:28709](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28709) · Entrez [84286](https://www.ncbi.nlm.nih.gov/gene/84286) · UniProt [Q9BSA9](https://www.uniprot.org/uniprotkb/Q9BSA9) · Ensembl [ENSG00000127419](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000127419)

## Data

Gene col 4808: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4808); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4808, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4808]; `tensor/DDL_lfc|DDL_z.npy` [4808]; `embed/gene_vectors.npy` [4808]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4808 or target_col == 4808). Every well: [[TMEM175 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM175.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
