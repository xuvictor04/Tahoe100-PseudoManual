---
symbol: "DNAH1"
type: "gene"
col: 3593
ensembl_id: "ENSG00000114841"
name: "dynein axonemal heavy chain 1"
location: "3p21.1"
module: 47
arm: "+"
pooled_cpm: 9.26
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 18
n_dd_up_clean: 1
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/047"]
generated_by: "tahoemap"
---

# DNAH1

*dynein axonemal heavy chain 1* — 3p21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[Demeclocycline (drug)]] 5 µM: 1.31× (z +3.9, q 0.059, up in 8 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (11 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.598× (z -7.5, q 3e-11, down in 26 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZDHHC11]] (+0.67, fdr 7e-06), [[RNF32-AS1]] (+0.66, fdr 7e-06), [[FSCN2]] (+0.62, fdr 1e-05); moves opposite to [[RCOR3]] (-0.64, fdr 7e-06), [[CNIH4]] (-0.59, fdr 1e-05), [[ACTR10]] (-0.56, fdr 1e-05).
> It is in [[Module 047]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3593.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Demeclocycline (drug)]] 5 µM |  | **1.31×** | +3.9 | 0.059 | 8/47 (HCT15, A549, …) | top dose only | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | 1.41× | +3.5 | 0.11 | 18/46 (C32, RKO, …) | top dose only | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.10× | +3.5 | 0.11 | 2/48 (RPMI-7951, SW48) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | 1.24× | +3.0 | 0.34 | 15/45 (C32, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 11 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3593.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **0.598×** | -7.5 | 3e-11 | 26/46 (SNU-423, Panc 03.27, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.510×** | -7.0 | 8e-10 | 29/43 (LoVo, SW480, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.527×** | -6.6 | 6e-09 | 27/47 (NCI-H1573, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.495×** | -6.4 | 3e-08 | 28/45 (SW480, LS 180, …) | two highest doses | cell-cycle shift (explains ~11% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.582×** | -5.4 | 6e-06 | 22/46 (SW480, HEC-1-A, …) | two highest doses | composition shift; position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.594×** | -5.4 | 6e-06 | 24/46 (HCT15, HOP62, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **0.592×** | -5.2 | 1e-05 | 25/38 (NCI-H1573, HOP62, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.451×** | -4.3 | 0.001 | 20/44 (A-427, SNU-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~19% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.662×** | -4.3 | 0.001 | 22/46 (SW480, KATO III, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | **0.759×** | -4.1 | 0.003 | 16/46 (RKO, NCI-H1792, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.688×** | -3.9 | 0.005 | 21/45 (H4, LoVo, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.680×** | -3.9 | 0.005 | 21/39 (HT-29, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.691×** | -3.8 | 0.005 | 20/46 (RPMI-7951, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.682×** | -3.8 | 0.005 | 18/43 (A-427, RPMI-7951, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.715×** | -3.5 | 0.018 | 17/45 (RPMI-7951, SW480, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.753×** | -3.0 | 0.096 | 14/46 (AsPC-1, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3593. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 12.0 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0441× (z -18.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[SW480 (line)]] | alt | 21.4 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0913× (z -17.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[A-427 (line)]] | wt | 14.0 | 0 | 2 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.120× (z -10.6) ⚠ cell-cycle shift, explains ~40% of this change |
| [[BT-474 (line)]] | alt | 7.47 | 0 | 2 (1 ⚠) | — | [[Penfluridol (drug)]] 0.05 µM 0.0762× (z -8.8) |
| [[HT-29 (line)]] | alt | 10.8 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.182× (z -11.2) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H1573 (line)]] | alt | 4.58 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0367× (z -11.8) ⚠ cell-cycle shift, explains ~32% of this change |
| [[SNU-423 (line)]] | alt | 7.89 | 0 | 2 | — | [[Selinexor (drug)]] 5 µM 0.181× (z -9.9) |
| [[A-172 (line)]] | wt | 5.98 | 0 | 1 | — | [[Posaconazole (drug)]] 0.05 µM 0.0629× (z -10.0) |
| [[C-33 A (line)]] | alt | 8.71 | 0 | 1 | — | [[Azithromycin (hydrate) (drug)]] 0.5 µM 0.0521× (z -9.8) |
| [[KATO III (line)]] | alt | 7.74 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0486× (z -12.9) ⚠ cell-cycle shift, explains ~36% of this change |
| [[NCI-H23 (line)]] | alt | 14.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.171× (z -8.8) ⚠ cell-cycle shift, explains ~36% of this change |
| [[NCI-H2347 (line)]] | alt | 3.96 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.0806× (z -9.2) ⚠ toxic |
| [[NCI-H460 (line)]] | wt | 9.84 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.177× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[RKO (line)]] | wt | 8.95 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.119× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[RPMI-7951 (line)]] | alt | 14.7 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.132× (z -8.9) |
| [[SW1417 (line)]] | alt | 8.64 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0683× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[A498 (line)]] | wt | 4.30 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.50 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.28 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.51 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.42 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.78 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.35 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.35 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.88 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.43 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.64 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.73 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.09 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.78 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.65 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.98 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.73 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.33 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.19 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.43 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.46 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.53 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.81 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.06 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 19.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.54 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.64 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3593), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZDHHC11]] | +0.67 | +0.68 / +0.62 | both halves | 7e-06 |  |
| [[RNF32-AS1]] | +0.66 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[FSCN2]] | +0.62 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[ABR]] | +0.61 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[THOC6]] | +0.60 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[SLC9A5]] | +0.60 | +0.57 / +0.62 | both halves | 9e-06 |  |
| [[MC1R]] | +0.59 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[CHRNA10]] | +0.59 | +0.60 / +0.47 | both halves | 2e-05 |  |
| [[MMP25]] | +0.59 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[CFAP161]] | +0.58 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[CHADL]] | +0.58 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[CYP2D7]] | +0.57 | +0.44 / +0.62 | both halves | 3e-05 |  |

## Genes that move opposite

*38 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RCOR3]] | -0.64 | -0.62 / -0.60 | both halves | 7e-06 |  |
| [[CNIH4]] | -0.59 | -0.55 / -0.53 | both halves | 1e-05 |  |
| [[ACTR10]] | -0.56 | -0.51 / -0.59 | both halves | 1e-05 |  |
| [[TRAPPC11]] | -0.56 | -0.48 / -0.60 | both halves | 2e-05 |  |
| [[TATDN3]] | -0.56 | -0.42 / -0.61 | both halves | 4e-05 |  |
| [[PRMT9]] | -0.55 | -0.47 / -0.58 | both halves | 2e-05 |  |
| [[NDFIP1]] | -0.55 | -0.60 / -0.46 | both halves | 3e-05 |  |
| [[SLC35A1]] | -0.55 | -0.52 / -0.51 | both halves | 1e-05 |  |
| [[NIPSNAP2]] | -0.55 | -0.46 / -0.58 | both halves | 2e-05 |  |
| [[CCZ1]] | -0.54 | -0.57 / -0.44 | both halves | 3e-05 |  |
| [[PEX3]] | -0.54 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[LAMTOR2]] | -0.54 | -0.49 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 047]]; 95 genes; every member is in the + arm (projection on the module's main direction 0.636). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (37.1, -10.5); signed map (20.3, 15.7). **Vector** length 73.0, 12.8% of its response variance represented; |z| ≥ 3 in 960 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +6.0 | +3.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +4.6 | -0.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.5 | +0.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.2 | -0.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.9 | +3.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | +0.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.2 | +2.6 |
|  | [[Demeclocycline (drug)]] 5 µM |  | +1.7 | +3.9 |
|  | [[Omeprazole (drug)]] 0.05 µM |  | +1.5 | +2.8 |
| fall | [[Selinexor (drug)]] 5 µM |  | -4.3 | -7.5 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.9 | -1.7 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.8 | -4.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.3 | -1.9 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | -1.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.0 | -1.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.8 | -2.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.7 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | dynein axonemal heavy chain 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p21.1 — chr3:52,316,319-52,400,492 (+) |
| Ensembl biotype | protein_coding |
| Also known as | XLHSRF-1, DNAHC1, HDHC7, HL-11, HL11 |
| Gene groups (HGNC) | Dyneins, axonemal inner arm I1/f complex subunits; Dynein heavy chains |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P2D7](https://www.uniprot.org/uniprotkb/Q9P2D7) (Dynein axonemal heavy chain 1):

> Force generating protein of cilia required for sperm flagellum motility. Produces force towards the minus ends of microtubules. Dynein has ATPase activity; the force-producing power stroke is thought to occur on release of ADP. Required in spermatozoa for the formation of the inner dynein arms and biogenesis of the axoneme.

**Summary**, from NCBI Gene [25981](https://www.ncbi.nlm.nih.gov/gene/25981):

> This gene encodes an inner dynein arm heavy chain that provides structural support between the radial spokes and the outer doublet of the sperm tail. Naturally occurring mutations in this gene are associated with primary ciliary dyskinesia and multiple morphological anomalies of the flagella that result in asthenozoospermia and male infertility. Mice with a homozygous knockout of the orthologous gene are viable but have reduced sperm motility and are infertile. [provided by RefSeq, Feb 2017]

**Accessions** — [HGNC:2940](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2940) · Entrez [25981](https://www.ncbi.nlm.nih.gov/gene/25981) · UniProt [Q9P2D7](https://www.uniprot.org/uniprotkb/Q9P2D7) · Ensembl [ENSG00000114841](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000114841)

## Data

Gene col 3593: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3593); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3593, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3593]; `tensor/DDL_lfc|DDL_z.npy` [3593]; `embed/gene_vectors.npy` [3593]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3593 or target_col == 3593). Every well: [[DNAH1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DNAH1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
