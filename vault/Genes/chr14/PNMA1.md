---
symbol: "PNMA1"
type: "gene"
col: 10763
ensembl_id: "ENSG00000176903"
name: "PNMA family member 1"
location: "14q24.3"
module: 7
arm: "+"
pooled_cpm: 13.46
n_lines_expressing: 49
n_dd_up: 6
n_dd_down: 11
n_dd_up_clean: 5
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# PNMA1

*PNMA family member 1* — 14q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.27× (z +4.5, q 0.003, up in 18 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.597× (z -9.6, q 5e-19, down in 31 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FEM1B]] (+0.58, fdr 1e-05), [[ADAMTSL5]] (+0.57, fdr 1e-05), [[ASB6]] (+0.57, fdr 2e-05); moves opposite to [[CCDC170]] (-0.50, fdr 5e-05), [[MCCC1]] (-0.48, fdr 3e-05), [[TIAL1]] (-0.48, fdr 9e-05).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10763.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **1.27×** | +4.5 | 0.003 | 18/47 (NCI-H1573, MIA PaCa-2, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~3% here); position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.40×** | +4.4 | 0.003 | 18/46 (NCI-H460, SW 900, …) | rises with dose | low cells (technical?) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.38×** | +4.1 | 0.007 | 16/46 (RPMI-7951, LS 180, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.34×** | +3.8 | 0.019 | 13/46 (MIA PaCa-2, NCI-H2347, …) | top dose only | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.33×** | +3.6 | 0.031 | 13/37 (KATO III, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.47×** | +3.6 | 0.031 | 7/39 (RKO, LOX-IMVI, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.27× | +3.2 | 0.11 | 7/47 (HOP62, MIA PaCa-2, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10763.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.597×** | -9.6 | 5e-19 | 31/45 (NCI-H460, LS 180, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.744×** | -5.5 | 1e-05 | 23/45 (AsPC-1, A-172, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.515×** | -4.6 | 9e-04 | 18/32 (Panc 03.27, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | **0.699×** | -4.5 | 9e-04 | 19/46 (SW 900, LOX-IMVI, …) | top dose only | position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.715×** | -4.2 | 0.003 | 15/46 (NCI-H460, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.731×** | -4.1 | 0.004 | 17/47 (LoVo, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.779×** | -3.3 | 0.081 | 12/47 (SNU-423, COLO 205, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.623×** | -3.2 | 0.081 | 12/47 (J82, LS 180, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.709×** | -3.2 | 0.081 | 13/47 (HS-578T, NCI-H1573, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~18% of this change | **0.785×** | -3.2 | 0.084 | 14/43 (AsPC-1, LoVo, …) | inconsistent across doses | position effect removed |
| [[Gemcitabine (drug)]] 0.5 µM |  | **0.790×** | -3.1 | 0.093 | 9/47 (RPMI-7951, Hs 766T, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10763. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 26.9 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.224× (z -12.0) |
| [[NCI-H23 (line)]] | alt | 19.1 | 0 | 3 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0990× (z -13.2) ⚠ toxic; cell-cycle shift, explains ~15% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.309× (z -9.9) |
| [[BT-474 (line)]] | alt | 17.6 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.119× (z -11.2) ⚠ toxic; cell-cycle shift, explains ~15% of this change |
| [[LoVo (line)]] | wt | 14.7 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.107× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.332× (z -8.7) |
| [[LS 180 (line)]] | wt | 12.1 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.193× (z -11.2) |
| [[NCI-H460 (line)]] | wt | 25.5 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.277× (z -12.2) |
| [[A-172 (line)]] | wt | 27.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.341× (z -11.0) |
| [[A-427 (line)]] | wt | 20.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.230× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 9.76 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.0634× (z -12.5) |
| [[C-33 A (line)]] | alt | 15.4 | 0 | 1 (1 ⚠) | — | [[Pimozide (drug)]] 0.5 µM 0.0984× (z -10.7) ⚠ transcription drop |
| [[HepG2_C3A (line)]] | wt | 14.1 | 0 | 1 | — | [[Sulfatinib (drug)]] 5 µM 0.0573× (z -10.9) |
| [[HS-578T (line)]] | alt | 12.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -8.9) |
| [[LOX-IMVI (line)]] | wt | 10.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.106× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 16.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.347× (z -9.3) |
| [[NCI-H1573 (line)]] | alt | 13.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.127× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H2347 (line)]] | alt | 18.0 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.395× (z -9.5) |
| [[SHP-77 (line)]] | alt | 12.3 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.117× (z -10.7) |
| [[SNU-423 (line)]] | alt | 9.58 | 0 | 1 (1 ⚠) | — | [[Nimesulide (drug)]] 5 µM 0.159× (z -9.2) ⚠ toxic; unreliable plate only |
| [[SW48 (line)]] | wt | 14.0 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0540× (z -11.0) ⚠ toxic; cell-cycle shift, explains ~15% of this change |
| [[A498 (line)]] | wt | 4.49 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.49 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.18 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.56 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.70 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.18 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.61 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.57 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.57 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.63 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 10.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10763), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FEM1B]] | +0.58 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[ADAMTSL5]] | +0.57 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[ASB6]] | +0.57 | +0.53 / +0.47 | both halves | 2e-05 |  |
| [[YWHAH]] | +0.55 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[ELOVL1]] | +0.55 | +0.54 / +0.45 | both halves | 3e-05 |  |
| [[ATMIN]] | +0.54 | +0.47 / +0.61 | both halves | 2e-05 |  |
| [[CPTP]] | +0.54 | +0.57 / +0.42 | both halves | 4e-05 |  |
| [[TUBA1A]] | +0.54 | +0.49 / +0.49 | both halves | 1e-05 |  |
| [[RHOC]] | +0.54 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[ATXN7L3]] | +0.53 | +0.41 / +0.52 | both halves | 4e-05 |  |
| [[BCKDK]] | +0.52 | +0.44 / +0.52 | both halves | 3e-05 |  |
| [[UBL4A]] | +0.52 | +0.49 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC170]] | -0.50 | -0.39 / -0.41 | both halves | 5e-05 |  |
| [[MCCC1]] | -0.48 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[TIAL1]] | -0.48 | -0.36 / -0.46 | both halves | 9e-05 |  |
| [[FAM217A]] | -0.48 | -0.42 / -0.40 | both halves | 5e-05 |  |
| [[COG7]] | -0.46 | -0.38 / -0.42 | both halves | 7e-05 |  |
| [[MIA]] | -0.46 | -0.48 / -0.28 | both halves | 3e-04 |  |
| [[PP2D1]] | -0.45 | -0.43 / -0.33 | both halves | 1e-04 |  |
| [[MYO3B]] | -0.45 | -0.41 / -0.33 | both halves | 1e-04 |  |
| [[C2CD5-AS1]] | -0.45 | -0.44 / -0.33 | both halves | 1e-04 |  |
| [[LRRC37A16P]] | -0.45 | -0.44 / -0.36 | both halves | 1e-04 |  |
| [[FLJ40194]] | -0.45 | -0.43 / -0.33 | both halves | 1e-04 |  |
| [[FAM184B]] | -0.45 | -0.45 / -0.32 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.328). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (16.3, -1.9); signed map (-8.7, 28.2). **Vector** length 78.8, 13.9% of its response variance represented; |z| ≥ 3 in 904 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.3 | +3.2 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.1 | +2.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.7 | +4.4 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | +2.7 | -0.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.6 | +3.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.3 | +2.5 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +1.8 | +0.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.6 | +0.2 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.9 | -9.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -3.5 | -0.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.3 | -5.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.1 | -0.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -3.1 | +1.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | -3.0 | -4.5 |
|  | [[EX229 (drug)]] 5 µM |  | -1.9 | -2.0 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -1.7 | -1.5 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | -1.5 | -1.1 |
|  | [[Budesonide (drug)]] 0.05 µM |  | -1.5 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | PNMA family member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q24.3 — chr14:73,711,783-73,714,384 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MA1 |
| Gene groups (HGNC) | Paraneoplastic Ma antigens |
| Matched by | ensembl_id |

UniProt [Q8ND90](https://www.uniprot.org/uniprotkb/Q8ND90) carries no function annotation.

**Summary**, from NCBI Gene [9240](https://www.ncbi.nlm.nih.gov/gene/9240):

> This gene encodes a neuron- and testis-specific protein that is also expressed in some paraneoplastic syndromes affecting the nervous system. Some patients with neurologic disorders develop antibodies against the protein encoded by this gene. The identification of the antineuronal antibodies in the sera of these patients has facilitated the diagnosis of paraneoplastic neurological disorders and the early detection of the associated tumors. [provided by RefSeq, Feb 2014]

**Accessions** — [HGNC:9158](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9158) · Entrez [9240](https://www.ncbi.nlm.nih.gov/gene/9240) · UniProt [Q8ND90](https://www.uniprot.org/uniprotkb/Q8ND90) · Ensembl [ENSG00000176903](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000176903)

## Data

Gene col 10763: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10763); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10763, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10763]; `tensor/DDL_lfc|DDL_z.npy` [10763]; `embed/gene_vectors.npy` [10763]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10763 or target_col == 10763). Every well: [[PNMA1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PNMA1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
