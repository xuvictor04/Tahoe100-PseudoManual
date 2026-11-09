---
symbol: "ATM"
type: "gene"
col: 7365
ensembl_id: "ENSG00000149311"
name: "ATM serine/threonine kinase"
location: "11q22.3"
module: 42
arm: "+"
pooled_cpm: 190.65
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 40
n_dd_up_clean: 1
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 9
direction_downstream: 1
tags: ["gene", "module/042", "written"]
generated_by: "tahoemap"
---

# ATM

*ATM serine/threonine kinase* — 11q22.3

> [!summary] In one line
> ATM is the apical kinase of the DNA double-strand-break response and the kinase that phosphorylates p53 to begin its activation.

## What it is

ATM is a very large serine/threonine kinase of the phosphatidylinositol-3-kinase-related (PIKK) family. It is recruited to double-strand breaks by the MRE11-RAD50-NBS1 complex and, once active, phosphorylates hundreds of substrates on S/T-Q motifs: CHK2, H2AX, KAP1, SMC1, NBS1, BRCA1, 53BP1, MDM2 and p53 among them. Two of those matter directly for p53. Phosphorylation of p53 at Ser15 and phosphorylation of MDM2 and its partners together weaken the MDM2-p53 interaction and the degradation that normally keeps p53 at a low level, which is why p53 stabilises within minutes of a break rather than being newly transcribed. ATM also has a DNA-independent mode of activation by oxidative stress, which is biochemically distinct from the break-induced mode.

Biallelic loss of ATM causes ataxia-telangiectasia: progressive cerebellar degeneration, oculocutaneous telangiectasia, immunodeficiency, marked radiosensitivity and a high rate of lymphoid malignancy. Heterozygous carriers have moderately raised breast cancer risk, and ATM is a standard entry on hereditary cancer panels. Somatic ATM loss is common in chronic lymphocytic leukaemia, mantle cell lymphoma, and lung, prostate and pancreatic cancers, and is one of the better-studied contexts for ATR and PARP inhibitor sensitivity.

## What is uncertain

The textbook activation switch is contested. Autophosphorylation at Ser1981 with dissociation of an inactive dimer is the standard model from human cell work, but knock-in mice in which the equivalent serine cannot be phosphorylated activate Atm normally, so autophosphorylation is at least dispensable in mouse and may be a consequence rather than the cause of activation. The clean division of labour between ATM for double-strand breaks and ATR for replication stress is also a simplification: the kinases share substrates and partly compensate. For p53 specifically, ATM is one route to activation among several — nucleolar stress, oncogene-driven p14ARF and ribosomal protein signalling reach p53 without it — so ATM status does not predict p53 output in a given line. Finally, nothing in Tahoe-100M's design lets ATM's own functional status across the panel be read out.

## References

- Savitsky et al., 1995, Science — positional cloning of ATM as the gene mutated in ataxia-telangiectasia.
- Banin et al., 1998, Science — showed ATM phosphorylates p53 on Ser15 in the damage response.
- Bakkenist and Kastan, 2003, Nature — proposed activation by intermolecular autophosphorylation and dimer dissociation.
- Pellegrini et al., 2006, Nature — showed the corresponding autophosphorylation site is dispensable for murine Atm activation in vivo.
- Matsuoka et al., 2007, Science — mapped the large ATM/ATR substrate landscape by phosphoproteomics.
- Shiloh and Ziv, 2013, Nature Reviews Molecular Cell Biology — review of ATM signalling, including its oxidative-stress mode.

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[GSK1059615 (drug)]] 5 µM: 1.54× (z +3.9, q 0.066, up in 31 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (SW48 3.92×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).
> Pooled over the cell lines (median), lowered significantly by 40 drug-doses (21 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.483× (z -17.6, q 0e+00, down in 42 of 48 measured lines) ⚠ cell-cycle shift, explains ~32% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.541× (z -10.5, q 1e-23, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PPIP5K2]] (+0.55, fdr 1e-05), [[APRG1]] (+0.55, fdr 1e-05), [[USO1]] (+0.54, fdr 1e-05); moves opposite to [[KRAS]] (-0.52, fdr 2e-05), [[B3GNT2]] (-0.50, fdr 4e-05), [[CRYBG2]] (-0.47, fdr 4e-05).
> It is in [[Module 042]], a single-armed module (UPR ER).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[CRYBG2]] → it (grade B ⚠); 1 goes from it, the strongest it → cells under [[Anethole trithione (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7365.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (SW48 3.92×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[GSK1059615 (drug)]] 5 µM |  | **1.54×** | +3.9 | 0.066 | 31/49 (A-427, NCI-H2347, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 5 µM |  | 1.40× | +3.0 | 0.76 | 21/49 (HEC-1-A, A-172, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 43 in all, 21 with an alert ⚠; shown: the 15 strongest and the 11 next strongest without an alert. 40 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 21 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7365.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.483×** | -17.6 | 0e+00 | 42/48 (SNU-423, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.417×** | -14.9 | 0e+00 | 47/48 (SW480, PANC-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.453×** | -13.5 | 2e-39 | 45/48 (SW480, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.454×** | -12.9 | 4e-36 | 42/48 (SNU-423, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.541×** | -10.5 | 1e-23 | 46/48 (KATO III, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.543×** | -10.4 | 2e-23 | 44/48 (SNU-1, RKO, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.544×** | -10.4 | 2e-23 | 42/48 (SW480, PANC-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.556×** | -10.0 | 9e-22 | 34/48 (AN3 CA, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.556×** | -10.0 | 9e-22 | 41/48 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.546×** | -9.9 | 2e-21 | 40/47 (KATO III, RKO, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.565×** | -9.7 | 1e-20 | 43/48 (SNU-1, hTERT-HPNE, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.674×** | -9.5 | 1e-19 | 40/49 (A549, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.582×** | -9.2 | 1e-18 | 42/48 (SNU-1, HCT15, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | **0.596×** | -8.5 | 1e-15 | 33/47 (Hs 766T, LoVo, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.609×** | -8.4 | 1e-15 | 45/48 (KATO III, PANC-1, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.418×** | -7.8 | 3e-13 | 44/49 (RKO, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~20% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.653×** | -7.3 | 1e-11 | 40/48 (NCI-H460, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.670×** | -6.4 | 4e-09 | 41/48 (KATO III, H4, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.503×** | -6.1 | 3e-08 | 38/48 (SW480, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.725×** | -5.5 | 1e-06 | 35/48 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose |  |
| [[venetoclax (drug)]] 5 µM |  | **0.576×** | -4.9 | 2e-05 | 39/48 (NCI-H460, A-427, …) | top dose only | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.837× | -4.3 | 4e-04 | 21/49 (CFPAC-1, Panc 03.27, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.805×** | -3.7 | 0.005 | 27/47 (CFPAC-1, Panc 03.27, …) | two highest doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.813×** | -3.5 | 0.008 | 22/48 (CFPAC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[EX229 (drug)]] 5 µM |  | **0.693×** | -3.3 | 0.019 | 24/48 (SW 900, HepG2/C3A, …) | rises with dose | noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **0.767×** | -3.2 | 0.021 | 26/48 (SK-MEL-2, COLO 205, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.31 per unit of S-phase module lfc, -0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7365. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 334 | 0 | 15 (11 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.193× (z -15.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.303× (z -11.5) |
| [[SW480 (line)]] | alt | 256 | 0 | 14 (12 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.209× (z -23.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.506× (z -10.1) |
| [[NCI-H460 (line)]] | wt | 167 | 0 | 13 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.373× (z -18.5) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.261× (z -17.9) |
| [[NCI-H1792 (line)]] | alt | 265 | 0 | 12 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.276× (z -21.2) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.406× (z -10.5) |
| [[PANC-1 (line)]] | alt | 373 | 0 | 12 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.318× (z -24.3) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.415× (z -13.2) |
| [[SNU-423 (line)]] | alt | 229 | 0 | 12 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -26.0) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.330× (z -12.9) |
| [[HOP62 (line)]] | alt | 180 | 0 | 10 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -17.7) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.357× (z -11.5) |
| [[hTERT-HPNE (line)]] | wt | 320 | 0 | 10 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.181× (z -21.7) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.182× (z -15.3) |
| [[KATO III (line)]] | alt | 296 | 0 | 9 (6 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.257× (z -15.3) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.259× (z -15.2) |
| [[MIA PaCa-2 (line)]] | alt | 250 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.241× (z -22.7) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.336× (z -12.3) |
| [[RPMI-7951 (line)]] | alt | 303 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.372× (z -15.8) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.346× (z -12.0) |
| [[Hs 766T (line)]] | wt | 252 | 0 | 8 (7 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.345× (z -11.2) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.394× (z -9.8) |
| [[J82 (line)]] | alt | 116 | 0 | 8 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -21.6) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.458× (z -9.5) |
| [[SNU-1 (line)]] | wt | 251 | 0 | 8 (7 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.256× (z -14.5) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.368× (z -10.6) |
| [[A549 (line)]] | wt | 168 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.297× (z -19.5) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.394× (z -14.9) |
| [[HCT15 (line)]] | alt | 278 | 0 | 7 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.293× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.367× (z -10.2) |
| [[HT-29 (line)]] | alt | 162 | 0 | 7 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.291× (z -12.6) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.350× (z -10.8) |
| [[RKO (line)]] | wt | 250 | 0 | 7 (6 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.342× (z -12.2) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.208× (z -9.3) |
| [[CFPAC-1 (line)]] | alt | 105 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.289× (z -18.0) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.366× (z -10.3) |
| [[SW 900 (line)]] | alt | 186 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.248× (z -21.0) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.280× (z -13.6) |
| [[A498 (line)]] | wt | 156 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.250× (z -20.0) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.255× (z -13.9) |
| [[AsPC-1 (line)]] | alt | 161 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.198× (z -23.4) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.357× (z -10.5) |
| [[SW1417 (line)]] | alt | 129 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.386× (z -14.7) ⚠ cell-cycle shift, explains ~32% of this change |
| [[NCI-H1573 (line)]] | alt | 101 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.396× (z -13.1) |
| [[NCI-H23 (line)]] | alt | 189 | 0 | 4 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.411× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[HEC-1-A (line)]] | alt | 174 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.504× (z -12.8) ⚠ cell-cycle shift, explains ~32% of this change |
| [[HepG2_C3A (line)]] | wt | 166 | 0 | 3 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.391× (z -10.4) ⚠ cell-cycle shift, explains ~31% of this change |
| [[HS-578T (line)]] | alt | 211 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.426× (z -11.8) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.410× (z -8.7) |
| [[LoVo (line)]] | wt | 140 | 0 | 3 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.375× (z -10.4) ⚠ cell-cycle shift, explains ~31% of this change |
| [[LOX-IMVI (line)]] | wt | 243 | 0 | 3 (2 ⚠) | — | [[TAK-901 (drug)]] 0.05 µM 0.419× (z -10.7) |
| [[SK-MEL-2 (line)]] | alt | 156 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.328× (z -16.6) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.416× (z -9.3) |
| [[A-172 (line)]] | wt | 111 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.496× (z -11.1) ⚠ cell-cycle shift, explains ~32% of this change |
| [[C-33 A (line)]] | alt | 221 | 0 | 2 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.479× (z -8.9) |
| [[COLO 205 (line)]] | alt | 197 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.456× (z -11.5) ⚠ cell-cycle shift, explains ~32% of this change |
| [[Panc 03.27 (line)]] | alt | 125 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.418× (z -9.2) ⚠ cell-cycle shift, explains ~28% of this change |
| [[SHP-77 (line)]] | alt | 127 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.417× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[SW 1271 (line)]] | alt | 701 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.247× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[A-427 (line)]] | wt | 142 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.218× (z -17.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[AN3 CA (line)]] | alt | 154 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0864× (z -17.2) |
| [[BT-474 (line)]] | alt | 58.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.254× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[LS 180 (line)]] | wt | 98.5 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.365× (z -8.8) |
| [[SW48 (line)]] | wt | 104 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.92× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[C32 (line)]] | wt | 140 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 244 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 199 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 144 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 75.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 177 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 187 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 207 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7365), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPIP5K2]] | +0.55 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[APRG1]] | +0.55 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[USO1]] | +0.54 | +0.50 / +0.56 | both halves | 1e-05 | same gene group |
| [[SRP72]] | +0.51 | +0.34 / +0.60 | both halves | 1e-04 |  |
| [[CCNH]] | +0.48 | +0.49 / +0.47 | both halves | 2e-05 | pathway: TP53 Regulates Transcription of DNA Repair Genes; STRING 642 |
| [[SEC23IP]] | +0.47 | +0.42 / +0.54 | both halves | 4e-05 |  |
| [[AHI1]] | +0.47 | +0.44 / +0.43 | both halves | 3e-05 |  |
| [[TPP2]] | +0.47 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[CFAP44]] | +0.47 | +0.42 / +0.54 | both halves | 4e-05 |  |
| [[CDRT4]] | +0.46 | +0.46 / +0.49 | both halves | 2e-05 |  |
| [[MON2]] | +0.46 | +0.45 / +0.50 | both halves | 3e-05 | same gene group |
| [[FBXW8]] | +0.46 | +0.38 / +0.46 | both halves | 6e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KRAS]] | -0.52 | -0.48 / -0.52 | both halves | 2e-05 | STRING 718 |
| [[B3GNT2]] | -0.50 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[CRYBG2]] | -0.47 | -0.42 / -0.41 | both halves | 4e-05 |  |
| [[CBLC]] | -0.47 | -0.39 / -0.44 | both halves | 5e-05 |  |
| [[TTC9]] | -0.46 | -0.45 / -0.36 | both halves | 1e-04 |  |
| [[ABHD15]] | -0.46 | -0.39 / -0.42 | both halves | 5e-05 |  |
| [[HDHD3]] | -0.44 | -0.42 / -0.35 | both halves | 1e-04 |  |
| [[B4GALT5]] | -0.44 | -0.35 / -0.48 | both halves | 1e-04 |  |
| [[PROSER2]] | -0.43 | -0.36 / -0.45 | both halves | 1e-04 |  |
| [[IL22RA1]] | -0.43 | -0.39 / -0.43 | both halves | 5e-05 |  |
| [[PPP4R1]] | -0.43 | -0.40 / -0.42 | both halves | 5e-05 | same gene group |
| [[ARL8A]] | -0.43 | -0.32 / -0.42 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 9, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CRYBG2]] | B | CRYBG2 activity lowers ATM's level | lines that do not express CRYBG2 (23) vs lines expressing it (27) | 1.43× higher at baseline in the lines without CRYBG2 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: SPINT1-AS1, SMPDL3B, LAD1 |
| [[MISP]] | B | MISP activity lowers ATM's level | lines that do not express MISP (23) vs lines expressing it (27) | 1.47× higher at baseline in the lines without MISP | 0.013 | ⚠ within organs, on part of the lines; also absent: GRB7, KRT18, MYO5B |
| [[EPHA1]] | B | EPHA1 activity lowers ATM's level | lines that do not express EPHA1 (23) vs lines expressing it (27) | 1.41× higher at baseline in the lines without EPHA1 | 0.014 | ⚠ within organs, on part of the lines; also absent: TNNT2, KDF1, PLEKHG6; maybe low, not absent |
| [[NECTIN4]] | B | NECTIN4 activity lowers ATM's level | lines that do not express NECTIN4 (33) vs lines expressing it (17) | 1.58× higher at baseline in the lines without NECTIN4 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TMEM30B, PRSS8, RAB25 |
| [[KDF1]] | B | KDF1 activity lowers ATM's level | lines that do not express KDF1 (30) vs lines expressing it (20) | 1.49× higher at baseline in the lines without KDF1 | 0.019 | ⚠ within organs, on part of the lines; also absent: CDH1, ESRP1, CRB3 |
| [[GRHL3]] | B | GRHL3 activity lowers ATM's level | lines that do not express GRHL3 (16) vs lines expressing it (34) | 1.41× higher at baseline in the lines without GRHL3 | 0.057 | ⚠ within organs, on part of the lines; also absent: SPINT2, FA2H, CDC42BPG; maybe low, not absent |
| [[CBLC]] | B | CBLC activity weakens ATM's drug response | lines that do not express CBLC (31) vs lines expressing it (17) | the lines without CBLC respond 1.12× as strongly (z diff -1.23); strongest at Panobinostat 0.5 µM: 0.48x vs 0.65x (z diff -3.0) | 0.065 | ⚠ within organs, on part of the lines; also absent: KDF1, CLDN7, PRSS8; target measured in part of the lines; artifact flags |
| [[CBLC]] | B | CBLC activity lowers ATM's level | lines that do not express CBLC (31) vs lines expressing it (19) | 1.32× higher at baseline in the lines without CBLC | 0.067 | ⚠ within organs, on part of the lines; also absent: KDF1, CLDN7, PRSS8 |
| [[KDF1]] | B | KDF1 activity weakens ATM's drug response | lines that do not express KDF1 (30) vs lines expressing it (18) | the lines without KDF1 respond 1.14× as strongly (z diff -1.35); strongest at Panobinostat 0.5 µM: 0.47x vs 0.66x (z diff -3.4) | 0.076 | ⚠ within organs, on part of the lines; also absent: CDH1, ESRP1, CRB3; target measured in part of the lines; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Anethole trithione (drug)]] 0.5 µM | C | ATM's natural level raises the cells' numbers under Anethole trithione 0.5 µM (protects the cells) | ATM's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.60 | 0.472 over the table, 0.098 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 042]] — UPR ER; 103 genes; every member is in the + arm (projection on the module's main direction 0.333). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (24.5, -22.6); signed map (-58.0, 10.2). **Vector** length 95.7, 39.2% of its response variance represented; |z| ≥ 3 in 1,498 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[GSK1059615 (drug)]] 5 µM |  | +3.1 | +3.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.0 | -3.1 |
|  | [[Sapanisertib (drug)]] 5 µM |  | +2.8 | +3.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.5 | +0.9 |
|  | [[Gefitinib (drug)]] 5 µM |  | +2.5 | +1.0 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.4 | -9.5 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~64% of this change | -3.8 | -4.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.7 | -10.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.6 | -5.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.6 | -1.3 |
|  | [[venetoclax (drug)]] 5 µM |  | -3.6 | -4.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -3.4 | -0.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.4 | -0.8 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.2 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | ATM serine/threonine kinase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q22.3 — chr11:108,222,804-108,369,102 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TEL1, TELO1; previously ATA, ATDC, ATC, ATD |
| Gene groups (HGNC) | Armadillo like helical domain containing; Phosphatidylinositol 3-kinase-related kinase family; BRCA1-associated genome surveillance complex |
| Reactome | 57 pathways, smallest: Sensing of DNA Double Strand Breaks; TP53 Regulates Transcription of Caspase Activators and Caspases; Pexophagy |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13315](https://www.uniprot.org/uniprotkb/Q13315) (Serine-protein kinase ATM):

> Serine/threonine protein kinase which activates checkpoint signaling upon double strand breaks (DSBs), apoptosis and genotoxic stresses such as ionizing ultraviolet A light (UVA), thereby acting as a DNA damage sensor. Recognizes the substrate consensus sequence [ST]-Q. Phosphorylates 'Ser-139' of histone variant H2AX at double strand breaks (DSBs), thereby regulating DNA damage response mechanism (By similarity). Also plays a role in pre-B cell allelic exclusion, a process leading to …

**Summary**, from NCBI Gene [472](https://www.ncbi.nlm.nih.gov/gene/472):

> The protein encoded by this gene belongs to the PI3/PI4-kinase family. This protein is an important cell cycle checkpoint kinase that phosphorylates; thus, it functions as a regulator of a wide variety of downstream proteins, including tumor suppressor proteins p53 and BRCA1, checkpoint kinase CHK2, checkpoint proteins RAD17 and RAD9, and DNA repair protein NBS1. This protein and the closely related kinase ATR are thought to be master controllers of cell cycle checkpoint signaling pathways that …

**Accessions** — [HGNC:795](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:795) · Entrez [472](https://www.ncbi.nlm.nih.gov/gene/472) · UniProt [Q13315](https://www.uniprot.org/uniprotkb/Q13315) · Ensembl [ENSG00000149311](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000149311)

## Data

Gene col 7365: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7365); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7365, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7365]; `tensor/DDL_lfc|DDL_z.npy` [7365]; `embed/gene_vectors.npy` [7365]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7365 or target_col == 7365). Every well: [[ATM — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. The written part above is `tahoemap/vault_seed/genes/ATM.md`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
