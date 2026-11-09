---
symbol: "KLHDC4"
type: "gene"
col: 2490
ensembl_id: "ENSG00000104731"
name: "kelch domain containing 4"
location: "16q24.2"
module: 5
arm: "+"
pooled_cpm: 45.37
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 6
n_dd_up_clean: 13
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# KLHDC4

*kelch domain containing 4* — 16q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (7 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 1.97× (z +10.8, q 1e-24, up in 45 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 3.32× (z +9.5, q 5e-19, up in 40 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Carbidopa (monohydrate) (drug)]] 0.05 µM: 0.774× (z -4.1, q 0.014, down in 22 of 48 measured lines) ⚠ unreliable plate only; position not correctable. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.834× (z -4.1, q 0.014, down in 24 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WDR4]] (+0.78, fdr 7e-06), [[MDN1]] (+0.77, fdr 7e-06), [[POLR1A]] (+0.75, fdr 7e-06); moves opposite to [[LCA5]] (-0.58, fdr 1e-05), [[KDM5B]] (-0.58, fdr 2e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2490.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.97×** | +10.8 | 1e-24 | 45/48 (NCI-H460, MIA PaCa-2, …) | all doses, flat |  |
| [[TAK-901 (drug)]] 5 µM |  | **3.32×** | +9.5 | 5e-19 | 40/49 (HOP62, COLO 205, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.54×** | +7.4 | 2e-11 | 35/47 (RKO, LOX-IMVI, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **1.48×** | +6.3 | 4e-08 | 28/48 (HOP62, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.43×** | +5.7 | 1e-06 | 28/48 (NCI-H2030, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.39×** | +5.1 | 4e-05 | 28/47 (NCI-H1573, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[EX229 (drug)]] 5 µM |  | **1.83×** | +4.8 | 1e-04 | 29/47 (MIA PaCa-2, LOX-IMVI, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.75×** | +4.5 | 6e-04 | 26/47 (A498, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.33×** | +4.2 | 0.002 | 23/44 (HT-29, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~2% here); composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **1.31×** | +4.2 | 0.002 | 22/48 (NCI-H1573, HS-578T, …) | top dose only |  |
| [[venetoclax (drug)]] 5 µM |  | **1.67×** | +4.1 | 0.003 | 18/47 (A498, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.62×** | +3.8 | 0.006 | 14/34 (A549, NCI-H1573, …) | rises with dose | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.27×** | +3.8 | 0.006 | 22/48 (NCI-H1573, SW 900, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[TAK-733 (drug)]] 5 µM |  | **1.57×** | +3.6 | 0.013 | 16/47 (A498, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.25×** | +3.6 | 0.014 | 19/48 (HS-578T, HOP62, …) | rises with dose | position effect removed |
| [[Budesonide (drug)]] 5 µM |  | **1.23×** | +3.3 | 0.036 | 15/48 (AsPC-1, A498, …) | top dose only |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.22×** | +3.2 | 0.038 | 11/47 (LOX-IMVI, NCI-H460, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.21×** | +3.0 | 0.078 | 20/48 (NCI-H1792, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2490.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.774×** | -4.1 | 0.014 | 22/48 (SW480, BT-474, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.834× | -4.1 | 0.014 | 24/48 (KATO III, LS 180, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.795×** | -3.7 | 0.036 | 17/46 (SNU-1, SW48, …) | inconsistent across doses | cell-cycle shift (explains ~9% here); composition shift |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.799×** | -3.6 | 0.036 | 18/47 (SK-MEL-2, MIA PaCa-2, …) | inconsistent across doses |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.636×** | -3.6 | 0.036 | 17/47 (NCI-H2347, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.805×** | -3.5 | 0.046 | 21/48 (SW 1271, LS 180, …) | rises with dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Entrectinib (drug)]] 5 µM |  | **0.818×** | -3.2 | 0.099 | 21/47 (CFPAC-1, MIA PaCa-2, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, -0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2490. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 14.9 | 11 | 1 | [[Clobetasol propionate (drug)]] 0.05 µM 7.34× (z +11.1) | [[Imiquimod (maleate) (drug)]] 5 µM 0.178× (z -9.3) |
| [[NCI-H1573 (line)]] | alt | 46.5 | 3 | 0 | [[Clobetasol propionate (drug)]] 0.05 µM 3.25× (z +9.5) | — |
| [[A-427 (line)]] | wt | 62.1 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -18.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 98.3 | 1 (1 ⚠) | 1 (1 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.78× (z +9.3) ⚠ unreliable plate only | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.278× (z -16.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 77.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.187× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 43.0 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.54× (z +9.3) ⚠ unreliable plate only | — |
| [[H4 (line)]] | wt | 49.3 | 0 | 1 | — | [[Pimozide (drug)]] 0.05 µM 0.233× (z -8.6) |
| [[HCT15 (line)]] | alt | 34.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.144× (z -11.7) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 21.7 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 4.33× (z +8.7) ⚠ unreliable plate only | — |
| [[hTERT-HPNE (line)]] | wt | 17.9 | 0 | 1 | — | [[Hydroxyurea (drug)]] 0.05 µM 0.101× (z -10.0) |
| [[KATO III (line)]] | alt | 75.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.363× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1792 (line)]] | alt | 30.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.23× (z +12.1) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H460 (line)]] | wt | 26.5 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 3.10× (z +9.5) ⚠ unreliable plate only | — |
| [[SK-MEL-2 (line)]] | alt | 80.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.327× (z -10.1) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 67.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.141× (z -13.7) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 64.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.174× (z -12.5) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 45.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 45.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 62.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 61.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 47.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 35.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 29.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 44.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 30.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 37.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 38.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 35.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 41.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 92.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 44.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 38.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 54.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 56.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 80.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 39.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 35.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 49.8 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 63.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2490), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WDR4]] | +0.78 | +0.76 / +0.77 | both halves | 7e-06 |  |
| [[MDN1]] | +0.77 | +0.73 / +0.78 | both halves | 7e-06 |  |
| [[POLR1A]] | +0.75 | +0.73 / +0.72 | both halves | 7e-06 |  |
| [[HEATR1]] | +0.75 | +0.75 / +0.73 | both halves | 7e-06 |  |
| [[PUM3]] | +0.73 | +0.70 / +0.72 | both halves | 7e-06 |  |
| [[PUS1]] | +0.72 | +0.67 / +0.72 | both halves | 7e-06 |  |
| [[MYBBP1A]] | +0.72 | +0.70 / +0.71 | both halves | 7e-06 |  |
| [[URB2]] | +0.72 | +0.75 / +0.69 | both halves | 7e-06 |  |
| [[GNL3L]] | +0.71 | +0.68 / +0.75 | both halves | 7e-06 |  |
| [[DDX54]] | +0.71 | +0.71 / +0.68 | both halves | 7e-06 |  |
| [[SP2-AS1]] | +0.70 | +0.65 / +0.69 | both halves | 7e-06 |  |
| [[NOL10]] | +0.70 | +0.67 / +0.73 | both halves | 7e-06 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LCA5]] | -0.58 | -0.50 / -0.54 | both halves | 1e-05 |  |
| [[KDM5B]] | -0.58 | -0.48 / -0.63 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.710). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-12.6, -36.2); signed map (-4.5, -50.1). **Vector** length 113, 29.4% of its response variance represented; |z| ≥ 3 in 896 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *MYC targets v2* (hallmark, mean cos +0.57 to 13); *rRNA processing* (reactome, mean cos +0.52 to 20); *rRNA processing in the nucleus and cytosol* (reactome, mean cos +0.52 to 19).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +8.5 | +10.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +5.9 | +4.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.7 | +7.4 |
|  | [[EX229 (drug)]] 5 µM |  | +4.5 | +4.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +4.5 | +4.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | +3.9 | +3.6 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -4.5 | -4.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.3 | -1.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -4.2 | -3.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.2 | +1.2 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.7 | -2.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.5 | -3.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.1 | -1.8 |
|  | [[Entrectinib (drug)]] 5 µM |  | -1.9 | -3.2 |
|  | [[Glycyrrhizic acid (drug)]] 5 µM |  | -1.7 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | kelch domain containing 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q24.2 — chr16:87,696,485-87,765,992 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp434G0522 |
| Matched by | ensembl_id |

UniProt [Q8TBB5](https://www.uniprot.org/uniprotkb/Q8TBB5) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:25272](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25272) · Entrez [54758](https://www.ncbi.nlm.nih.gov/gene/54758) · UniProt [Q8TBB5](https://www.uniprot.org/uniprotkb/Q8TBB5) · Ensembl [ENSG00000104731](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000104731)

## Data

Gene col 2490: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2490); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2490, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2490]; `tensor/DDL_lfc|DDL_z.npy` [2490]; `embed/gene_vectors.npy` [2490]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2490 or target_col == 2490). Every well: [[KLHDC4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KLHDC4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
