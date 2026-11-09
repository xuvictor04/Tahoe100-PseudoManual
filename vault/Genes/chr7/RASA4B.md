---
symbol: "RASA4B"
type: "gene"
col: 9993
ensembl_id: "ENSG00000170667"
name: "RAS p21 protein activator 4B"
location: "7q22.1"
module: 37
arm: "+"
pooled_cpm: 3.98
n_lines_expressing: 49
n_dd_up: 12
n_dd_down: 12
n_dd_up_clean: 10
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/037"]
generated_by: "tahoemap"
---

# RASA4B

*RAS p21 protein activator 4B* — 7q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.32× (z +12.6, q 2e-33, up in 37 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.469× (z -7.9, q 2e-12, down in 26 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PHF1]] (+0.68, fdr 1e-05), [[PHKG1]] (+0.68, fdr 7e-06), [[PPARA]] (+0.67, fdr 8e-06); moves opposite to [[FAIM]] (-0.62, fdr 3e-05), [[ATIC]] (-0.61, fdr 7e-06), [[FZD6]] (-0.60, fdr 1e-05).
> It is in [[Module 037]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9993.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.32×** | +12.6 | 2e-33 | 37/46 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.27×** | +12.4 | 7e-33 | 34/43 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **3.17×** | +12.1 | 3e-31 | 33/44 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.09×** | +10.9 | 1e-25 | 24/37 (A498, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.83×** | +6.3 | 3e-08 | 15/42 (LoVo, RKO, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.70×** | +5.3 | 8e-06 | 1/6 (NCI-H2347) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.59×** | +4.9 | 9e-05 | 14/45 (NCI-H2347, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.35×** | +4.5 | 4e-04 | 13/46 (NCI-H2347, KATO III, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.35×** | +4.5 | 4e-04 | 14/36 (PANC-1, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.41×** | +3.6 | 0.016 | 8/35 (NCI-H2347, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.82×** | +3.3 | 0.053 | 5/41 (PANC-1, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.36×** | +3.3 | 0.053 | 5/41 (HEC-1-A, A-427, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9993.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.469×** | -7.9 | 2e-12 | 26/44 (H4, hTERT-HPNE, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.326×** | -6.1 | 2e-07 | 22/38 (A498, hTERT-HPNE, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.610×** | -5.2 | 5e-05 | 14/42 (A-172, hTERT-HPNE, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.435×** | -4.5 | 7e-04 | 13/36 (SW480, KATO III, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.648×** | -4.5 | 7e-04 | 14/42 (H4, SW 900, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.672×** | -4.1 | 0.003 | 9/23 (LS 180, RKO, …) | all doses, flat | low cells (technical?); cell-cycle shift (explains ~4% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.900× | -3.9 | 0.006 | 14/47 (SNU-1, PANC-1, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.686×** | -3.9 | 0.006 | 10/43 (SW48, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.690×** | -3.9 | 0.007 | 13/45 (A-172, SW 900, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.700×** | -3.7 | 0.011 | 8/42 (A-427, H4, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.736×** | -3.2 | 0.071 | 10/44 (A-172, hTERT-HPNE, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.739×** | -3.2 | 0.077 | 10/46 (RKO, LoVo, …) | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 5 µM |  | **0.741×** | -3.1 | 0.077 | 5/44 (Hs 766T, SW 1271, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9993. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 13.0 | 0 | 4 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.179× (z -11.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.143× (z -8.9) |
| [[A498 (line)]] | wt | 6.94 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.86× (z +8.7) | [[Dinaciclib (drug)]] 0.05 µM 0.0831× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[c-Kit-IN-1 (drug)]] 5 µM 0.0460× (z -9.4) |
| [[CFPAC-1 (line)]] | alt | 2.27 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0450× (z -9.3) ⚠ cell-cycle shift, explains ~6% of this change |
| [[HCT15 (line)]] | alt | 10.4 | 0 | 1 | — | [[Elagolix sodium (drug)]] 0.5 µM 0.107× (z -8.8) |
| [[Hs 766T (line)]] | wt | 8.57 | 0 | 1 | — | [[Budesonide (drug)]] 0.5 µM 0.108× (z -8.5) |
| [[HT-29 (line)]] | alt | 5.59 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.0689× (z -10.5) ⚠ toxic |
| [[KATO III (line)]] | alt | 4.32 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0771× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 4.10 | 0 | 1 | — | [[Pemigatinib (drug)]] 0.05 µM 0.0540× (z -9.3) |
| [[A-427 (line)]] | wt | 2.31 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.61 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.25 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.41 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 52.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.80 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.61 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.96 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.93 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.66 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.09 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.24 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.10 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.36 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.05 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.765 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 5.71 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.64 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.32 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.01 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.18 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.46 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.61 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.89 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.31 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.26 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.84 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.16 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.95 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.45 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9993), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*57 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PHF1]] | +0.68 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[PHKG1]] | +0.68 | +0.67 / +0.72 | both halves | 7e-06 |  |
| [[PPARA]] | +0.67 | +0.58 / +0.64 | both halves | 8e-06 |  |
| [[TGFB1]] | +0.65 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[TESK2]] | +0.63 | +0.57 / +0.63 | both halves | 1e-05 |  |
| [[CCDC65]] | +0.60 | +0.52 / +0.65 | both halves | 1e-05 |  |
| [[TINCR]] | +0.59 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[ZNF473CR]] | +0.59 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[SPACDR]] | +0.59 | +0.52 / +0.68 | both halves | 1e-05 |  |
| [[ASMTL]] | +0.59 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[FAM89B]] | +0.59 | +0.41 / +0.55 | both halves | 4e-05 |  |
| [[TULP3]] | +0.58 | +0.60 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*43 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAIM]] | -0.62 | -0.45 / -0.59 | both halves | 3e-05 |  |
| [[ATIC]] | -0.61 | -0.58 / -0.58 | both halves | 7e-06 |  |
| [[FZD6]] | -0.60 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[ALG10B]] | -0.58 | -0.55 / -0.53 | both halves | 1e-05 |  |
| [[PPIL1]] | -0.58 | -0.50 / -0.57 | both halves | 1e-05 |  |
| [[ZNF239]] | -0.58 | -0.49 / -0.53 | both halves | 1e-05 |  |
| [[DCLRE1A]] | -0.58 | -0.42 / -0.58 | both halves | 4e-05 |  |
| [[ZNF252P-1]] | -0.58 | -0.33 / -0.68 | both halves | 1e-04 |  |
| [[IMPACT]] | -0.57 | -0.46 / -0.59 | both halves | 3e-05 |  |
| [[ZNF681]] | -0.57 | -0.35 / -0.52 | both halves | 1e-04 |  |
| [[ZFP62]] | -0.57 | -0.52 / -0.59 | both halves | 1e-05 |  |
| [[MTHFSD]] | -0.57 | -0.35 / -0.55 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 037]]; 123 genes; every member is in the + arm (projection on the module's main direction 0.516). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (27.9, -21.9); signed map (1.8, 27.8). **Vector** length 68.3, 10.8% of its response variance represented; |z| ≥ 3 in 1,065 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +4.1 | +6.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | +2.6 | +12.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.5 | +10.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.4 | +12.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~24% of this change | +2.3 | -0.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.1 | +4.5 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | +1.4 | +2.2 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | +1.3 | +0.9 |
|  | [[Vilanterol (drug)]] 5 µM |  | +1.3 | +2.3 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -4.3 | -7.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.5 | -5.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.7 | -3.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.4 | -1.8 |
|  | [[Budesonide (drug)]] 5 µM |  | -2.2 | -1.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.0 | -1.5 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -2.0 | -2.7 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.9 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | RAS p21 protein activator 4B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q22.1 — chr7:102,479,976-102,517,777 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Pleckstrin homology domain containing; C2 and RasGAP domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [C9J798](https://www.uniprot.org/uniprotkb/C9J798) (Ras GTPase-activating protein 4B):

> Ca(2+)-dependent Ras GTPase-activating protein, that may play a role in the Ras-MAPK pathway.

**Summary**, from NCBI Gene [100271927](https://www.ncbi.nlm.nih.gov/gene/100271927):

> Predicted to enable GTPase activator activity. Predicted to be involved in regulation of intracellular signal transduction. Predicted to be located in cytosol and plasma membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:35202](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:35202) · Entrez [100271927](https://www.ncbi.nlm.nih.gov/gene/100271927) · UniProt [C9J798](https://www.uniprot.org/uniprotkb/C9J798) · Ensembl [ENSG00000170667](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170667)

## Data

Gene col 9993: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9993); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9993, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9993]; `tensor/DDL_lfc|DDL_z.npy` [9993]; `embed/gene_vectors.npy` [9993]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9993 or target_col == 9993). Every well: [[RASA4B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RASA4B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
