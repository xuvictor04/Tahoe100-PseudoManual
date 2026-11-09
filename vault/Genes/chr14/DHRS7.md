---
symbol: "DHRS7"
type: "gene"
col: 2001
ensembl_id: "ENSG00000100612"
name: "dehydrogenase/reductase 7"
location: "14q23.1"
module: 3
arm: "+"
pooled_cpm: 61.4
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 11
n_dd_up_clean: 0
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# DHRS7

*dehydrogenase/reductase 7* — 14q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.82× (z +5.7, q 6e-06, up in 35 of 48 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.391× (z -13.4, q 5e-38, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 14 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MOB1B]] (+0.63, fdr 1e-05), [[CCDC126]] (+0.63, fdr 4e-05), [[NOP10]] (+0.60, fdr 5e-05, ⚠ NOP10 in the vector space only through flagged drug-doses), [[COMMD6]] (+0.60, fdr 2e-05); moves opposite to [[CBX5]] (-0.62, fdr 1e-05), [[HNRNPL]] (-0.59, fdr 7e-06), [[PTBP1]] (-0.54, fdr 1e-05).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 3 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2001.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.82×** | +5.7 | 6e-06 | 35/48 (KATO III, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.64×** | +4.8 | 4e-04 | 26/41 (LOX-IMVI, A498, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~27% of this change | **1.41×** | +3.5 | 0.079 | 29/48 (RPMI-7951, A-172, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 2 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2001.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.391×** | -13.4 | 5e-38 | 45/48 (AsPC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.457×** | -7.9 | 1e-12 | 45/48 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.469×** | -7.6 | 5e-12 | 42/48 (KATO III, RKO, …) | rises with dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.517×** | -6.6 | 5e-09 | 39/48 (KATO III, RKO, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.642×** | -4.4 | 0.001 | 27/48 (LOX-IMVI, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **0.778×** | -3.5 | 0.038 | 32/48 (LoVo, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.518×** | -3.5 | 0.045 | 26/49 (A-427, NCI-H2030, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.526×** | -3.4 | 0.053 | 24/48 (HOP62, LoVo, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.904× | -3.2 | 0.084 | 5/49 (NCI-H1792, NCI-H23, …) | inconsistent across doses |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.719×** | -3.2 | 0.086 | 25/49 (NCI-H2030, SW 900, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.730×** | -3.1 | 0.087 | 22/48 (SW 1088, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **0.557×** | -3.1 | 0.100 | 21/49 (A549, AsPC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Fusidic acid (drug)]] 5 µM |  | 0.807× | -3.0 | 0.11 | 24/48 (LS 180, NCI-H1792, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, +0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2001. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 105 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.117× (z -23.8) |
| [[KATO III (line)]] | alt | 31.2 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.196× (z -11.0) |
| [[RKO (line)]] | wt | 83.6 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.264× (z -9.7) |
| [[Panc 03.27 (line)]] | alt | 117 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.356× (z -12.5) |
| [[A498 (line)]] | wt | 96.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.424× (z -10.0) |
| [[A549 (line)]] | wt | 112 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.301× (z -12.9) |
| [[LoVo (line)]] | wt | 55.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.176× (z -18.1) |
| [[LOX-IMVI (line)]] | wt | 40.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.118× (z -14.4) |
| [[NCI-H1573 (line)]] | alt | 51.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.210× (z -15.2) |
| [[NCI-H2347 (line)]] | alt | 92.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.351× (z -14.1) |
| [[NCI-H460 (line)]] | wt | 63.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.290× (z -14.2) |
| [[SW480 (line)]] | alt | 35.1 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.223× (z -11.8) |
| [[A-427 (line)]] | wt | 33.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.216× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 83.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.238× (z -13.0) |
| [[CFPAC-1 (line)]] | alt | 97.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.239× (z -17.6) |
| [[COLO 205 (line)]] | alt | 24.9 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0603× (z -13.8) ⚠ toxic |
| [[HOP62 (line)]] | alt | 47.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -13.4) |
| [[HS-578T (line)]] | alt | 37.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.261× (z -13.2) |
| [[J82 (line)]] | alt | 47.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.359× (z -10.6) |
| [[LS 180 (line)]] | wt | 55.1 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.264× (z -9.1) |
| [[NCI-H2030 (line)]] | alt | 184 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.259× (z -15.9) |
| [[NCI-H23 (line)]] | alt | 92.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.279× (z -13.5) |
| [[SK-MEL-2 (line)]] | alt | 50.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.246× (z -12.9) |
| [[SNU-423 (line)]] | alt | 42.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.281× (z -12.4) |
| [[SW 1088 (line)]] | alt | 65.1 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0561× (z -9.1) |
| [[SW 1271 (line)]] | alt | 111 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -11.2) |
| [[A-172 (line)]] | wt | 48.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 63.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 49.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 42.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 39.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 61.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 64.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 42.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 23.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 58.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 54.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 52.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 64.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 56.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 39.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 44.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 53.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 44.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 52.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 41.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 93.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2001), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 14 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MOB1B]] | +0.63 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[CCDC126]] | +0.63 | +0.41 / +0.56 | both halves | 4e-05 |  |
| [[NOP10]] ⚠ | +0.60 | +0.40 / +0.71 | both halves | 5e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[COMMD6]] | +0.60 | +0.47 / +0.70 | both halves | 2e-05 |  |
| [[HEBP2]] | +0.59 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[SREK1IP1]] | +0.58 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[CAMLG]] | +0.58 | +0.53 / +0.67 | both halves | 1e-05 |  |
| [[ARL8A]] | +0.58 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[IL17RA]] | +0.57 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[ADPRM]] | +0.56 | +0.30 / +0.64 | both halves | 2e-04 |  |
| [[RPS27]] | +0.56 | +0.43 / +0.63 | both halves | 3e-05 |  |
| [[CCDC82]] | +0.56 | +0.45 / +0.54 | both halves | 3e-05 |  |
| [[ZNF600]] | +0.55 | +0.34 / +0.59 | both halves | 1e-04 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CBX5]] | -0.62 | -0.52 / -0.70 | both halves | 1e-05 |  |
| [[HNRNPL]] | -0.59 | -0.62 / -0.71 | both halves | 7e-06 |  |
| [[PTBP1]] | -0.54 | -0.50 / -0.57 | both halves | 1e-05 |  |
| [[ZNF628]] | -0.54 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[HNRNPD]] | -0.53 | -0.44 / -0.55 | both halves | 3e-05 |  |
| [[SRSF1]] | -0.53 | -0.52 / -0.63 | both halves | 1e-05 |  |
| [[SRP9]] | -0.51 | -0.27 / -0.57 | both halves | 3e-04 |  |
| [[FOXM1]] | -0.51 | -0.34 / -0.59 | both halves | 1e-04 |  |
| [[NCAPH2]] | -0.50 | -0.31 / -0.49 | both halves | 2e-04 |  |
| [[SAE1]] | -0.49 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[DNMT1]] | -0.49 | -0.43 / -0.52 | both halves | 4e-05 |  |
| [[MCM7]] | -0.49 | -0.41 / -0.50 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.421). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-41.4, -26.5); signed map (-23.2, 6.1). **Vector** length 90.6, 28.5% of its response variance represented; |z| ≥ 3 in 671 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.1 | +0.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.5 | +0.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +4.3 | +0.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.7 | +0.7 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.6 | +1.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.1 | +2.7 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.5 | +3.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.5 | +3.0 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +2.2 | +1.6 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.0 | +1.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.0 | -13.4 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.9 | -3.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -2.8 | +5.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -2.8 | -2.0 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | -1.9 | -0.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.9 | -0.1 |
|  | [[Balsalazide (sodium hydrate) (drug)]] 5 µM |  | -1.8 | -2.4 |
|  | [[Demeclocycline (drug)]] 5 µM |  | -1.7 | -2.9 |
|  | [[Clonidine (hydrochloride) (drug)]] 5 µM |  | -1.7 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | dehydrogenase/reductase 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q23.1 — chr14:60,144,119-60,169,856 (-) |
| Ensembl biotype | protein_coding |
| Also known as | retDSR4, SDR34C1 |
| Gene groups (HGNC) | Short chain dehydrogenase/reductase superfamily |
| Hallmark sets | XENOBIOTIC_METABOLISM, ADIPOGENESIS |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y394](https://www.uniprot.org/uniprotkb/Q9Y394) (Dehydrogenase/reductase SDR family member 7):

> NADPH-dependent oxidoreductase which catalyzes the reduction of a variety of compounds bearing carbonyl groups including steroids, retinoids and xenobiotics. Catalyzes the reduction/inactivation of 5alpha-dihydrotestosterone to 3alpha-androstanediol, with a possible role in the modulation of androgen receptor function. Involved in the reduction of all-trans-retinal to all-trans-retinol. Converts cortisone to 20beta-dihydrocortisone in vitro, although the physiological relevance of this activity …

**Summary**, from NCBI Gene [51635](https://www.ncbi.nlm.nih.gov/gene/51635):

> This gene encodes a member of the short-chain dehydrogenases/reductases (SDR) family, which has over 46,000 members. Members in this family are enzymes that metabolize many different compounds, such as steroid hormones, prostaglandins, retinoids, lipids and xenobiotics. [provided by RefSeq, Apr 2016]

**Accessions** — [HGNC:21524](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21524) · Entrez [51635](https://www.ncbi.nlm.nih.gov/gene/51635) · UniProt [Q9Y394](https://www.uniprot.org/uniprotkb/Q9Y394) · Ensembl [ENSG00000100612](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100612)

## Data

Gene col 2001: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2001); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2001, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2001]; `tensor/DDL_lfc|DDL_z.npy` [2001]; `embed/gene_vectors.npy` [2001]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2001 or target_col == 2001). Every well: [[DHRS7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DHRS7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
