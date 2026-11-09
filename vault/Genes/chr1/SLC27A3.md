---
symbol: "SLC27A3"
type: "gene"
col: 6771
ensembl_id: "ENSG00000143554"
name: "solute carrier family 27 member 3"
location: "1q21.3"
module: 80
arm: "+"
pooled_cpm: 3.05
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 19
n_dd_up_clean: 2
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/080"]
generated_by: "tahoemap"
---

# SLC27A3

*solute carrier family 27 member 3* — 1q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.03× (z +9.4, q 2e-18, up in 2 of 3 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.50× (z +5.1, q 6e-05, up in 8 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.274× (z -11.3, q 5e-27, down in 40 of 46 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PIGV]] (+0.57, fdr 1e-05), [[FBXO41]] (+0.55, fdr 8e-05), [[TEX264]] (+0.53, fdr 1e-05); moves opposite to [[RPS24]] (-0.47, fdr 7e-05), [[MTFR1]] (-0.46, fdr 3e-05), [[RPS25]] (-0.45, fdr 2e-04).
> It is in [[Module 080]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6771.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.03×** | +9.4 | 2e-18 | 2/3 (A498, CFPAC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.79×** | +5.2 | 6e-05 | 2/14 (HEC-1-A, LOX-IMVI) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.50×** | +5.1 | 6e-05 | 8/43 (SW480, KATO III, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~13% here); position effect removed |
| [[Filgotinib (drug)]] 5 µM |  | **1.53×** | +3.8 | 0.023 | 6/46 (A498, SK-MEL-2, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.51×** | +3.7 | 0.028 | 5/20 (A-427, SK-MEL-2, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 1 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6771.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.274×** | -11.3 | 5e-27 | 40/46 (NCI-H23, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.339×** | -9.5 | 7e-19 | 34/43 (LoVo, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.432×** | -7.4 | 4e-11 | 18/27 (SW480, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.449×** | -7.0 | 4e-10 | 27/43 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.461×** | -6.8 | 1e-09 | 22/43 (Panc 03.27, BT-474, …) | two highest doses | cell-cycle shift (explains ~9% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.485×** | -6.3 | 2e-08 | 23/43 (LOX-IMVI, MIA PaCa-2, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.529×** | -5.6 | 2e-06 | 19/43 (NCI-H2030, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.521×** | -5.4 | 5e-06 | 18/41 (SHP-77, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.558×** | -5.1 | 2e-05 | 21/44 (SHP-77, SW480, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.571×** | -4.9 | 6e-05 | 16/40 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.367×** | -4.6 | 2e-04 | 17/42 (HCT15, LS 180, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **0.620×** | -4.2 | 0.001 | 17/44 (SHP-77, NCI-H2347, …) | two highest doses | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.641×** | -3.9 | 0.005 | 17/44 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.662×** | -3.5 | 0.022 | 15/41 (BT-474, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift; position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **0.670×** | -3.3 | 0.031 | 12/34 (Hs 766T, A498, …) | top dose only | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.689×** | -3.2 | 0.043 | 15/43 (KATO III, Panc 03.27, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6771. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 6.81 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0584× (z -14.6) ⚠ cell-cycle shift, would explain all of this change |
| [[SHP-77 (line)]] | alt | 8.70 | 0 | 2 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0403× (z -12.7) |
| [[HCT15 (line)]] | alt | 9.32 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0768× (z -8.7) |
| [[LOX-IMVI (line)]] | wt | 3.97 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.0492× (z -9.8) |
| [[MIA PaCa-2 (line)]] | alt | 4.27 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.0458× (z -9.2) |
| [[NCI-H23 (line)]] | alt | 5.17 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0468× (z -11.5) |
| [[NCI-H2347 (line)]] | alt | 3.40 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.103× (z -8.6) |
| [[Panc 03.27 (line)]] | alt | 4.01 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0389× (z -10.4) |
| [[PANC-1 (line)]] | alt | 1.68 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0761× (z -9.0) |
| [[SW480 (line)]] | alt | 3.40 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0615× (z -11.9) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 4.25 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 5.57 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.39 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.953 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.964 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.44 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.94 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.13 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.16 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.52 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.26 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.12 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.42 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.19 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.76 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.10 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.869 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.71 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.66 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.48 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.78 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.42 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.90 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6771), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PIGV]] | +0.57 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[FBXO41]] | +0.55 | +0.59 / +0.37 | both halves | 8e-05 |  |
| [[TEX264]] | +0.53 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[PBX2]] | +0.52 | +0.51 / +0.47 | both halves | 2e-05 |  |
| [[SSH3]] | +0.52 | +0.50 / +0.43 | both halves | 3e-05 |  |
| [[TNS2]] | +0.52 | +0.48 / +0.45 | both halves | 3e-05 |  |
| [[CELSR3]] | +0.51 | +0.62 / +0.31 | both halves | 2e-04 |  |
| [[NEIL1]] | +0.51 | +0.45 / +0.52 | both halves | 3e-05 |  |
| [[ZC3H4]] | +0.50 | +0.61 / +0.32 | both halves | 2e-04 |  |
| [[ZNF747]] | +0.50 | +0.48 / +0.50 | both halves | 2e-05 |  |
| [[ZBTB45]] | +0.50 | +0.43 / +0.47 | both halves | 3e-05 |  |
| [[RGL2]] | +0.49 | +0.54 / +0.36 | both halves | 1e-04 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPS24]] | -0.47 | -0.49 / -0.38 | both halves | 7e-05 |  |
| [[MTFR1]] | -0.46 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[RPS25]] | -0.45 | -0.50 / -0.32 | both halves | 2e-04 |  |
| [[DAP3]] | -0.45 | -0.39 / -0.39 | both halves | 5e-05 |  |
| [[RPLP0]] | -0.45 | -0.45 / -0.35 | both halves | 1e-04 |  |
| [[RPL39]] | -0.44 | -0.41 / -0.36 | both halves | 1e-04 |  |
| [[GNA12]] | -0.44 | -0.55 / -0.26 | both halves | 4e-04 |  |
| [[PIP4K2A]] | -0.44 | -0.44 / -0.37 | both halves | 8e-05 |  |
| [[TPST2]] | -0.44 | -0.46 / -0.36 | both halves | 1e-04 |  |
| [[DOP1B]] | -0.43 | -0.39 / -0.41 | both halves | 5e-05 |  |
| [[RPS20]] | -0.43 | -0.40 / -0.36 | both halves | 1e-04 |  |
| [[EIF4E3]] | -0.43 | -0.42 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 080]]; 57 genes; every member is in the + arm (projection on the module's main direction 0.360). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-11.2, 32.8); signed map (12.9, -18.6). **Vector** length 50.6, 6.22% of its response variance represented; |z| ≥ 3 in 1,130 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.6 | -0.9 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.4 | +5.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.2 | +9.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.7 | +2.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.4 | +5.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.4 | +3.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.4 | +1.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.3 | +2.0 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +1.2 | +0.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.1 | +0.6 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.3 | -9.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.0 | -7.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.6 | -6.3 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -1.6 | -4.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | -1.6 | -3.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.5 | -1.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.2 | -3.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.2 | -3.3 |
|  | [[Loperamide (hydrochloride) (drug)]] 0.5 µM |  | -1.1 | -0.0 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 27 member 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q21.3 — chr1:153,774,354-153,780,157 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FATP3, MGC4365, ACSVL3 |
| Gene groups (HGNC) | Acyl-CoA synthetase family; Solute carrier family 27 |
| Reactome | 4 pathways, smallest: Synthesis of very long-chain fatty acyl-CoAs; Fatty acyl-CoA biosynthesis; Fatty acid metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5K4L6](https://www.uniprot.org/uniprotkb/Q5K4L6) (Long-chain fatty acid transport protein 3):

> Mainly functions as an acyl-CoA ligase catalyzing the ATP-dependent formation of fatty acyl-CoA using LCFA and very-long-chain fatty acids (VLCFA) as substrates. Can mediate the levels of long-chain fatty acids (LCFA) in the cell by facilitating their transport across membranes (By similarity).

**Summary**, from NCBI Gene [11000](https://www.ncbi.nlm.nih.gov/gene/11000):

> This gene belongs to a family of integral membrane proteins and encodes a protein that is involved in lipid metabolism. The increased expression of this gene in human neural stem cells derived from induced pluripotent stem cells suggests that it plays an important role in early brain development. Naturally occurring mutations in this gene are associated with autism spectrum disorders. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Feb 2017]

**Accessions** — [HGNC:10997](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10997) · Entrez [11000](https://www.ncbi.nlm.nih.gov/gene/11000) · UniProt [Q5K4L6](https://www.uniprot.org/uniprotkb/Q5K4L6) · Ensembl [ENSG00000143554](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143554)

## Data

Gene col 6771: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6771); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6771, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6771]; `tensor/DDL_lfc|DDL_z.npy` [6771]; `embed/gene_vectors.npy` [6771]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6771 or target_col == 6771). Every well: [[SLC27A3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC27A3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
